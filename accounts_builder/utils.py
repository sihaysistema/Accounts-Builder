from __future__ import unicode_literals

import frappe, json, os, tarfile
from frappe import _
from frappe.utils import cint, random_string
from frappe.utils import get_site_name, cstr
from unidecode import unidecode
from six import iteritems
from frappe.utils.nestedset import rebuild_tree


def get_chart(chart_template):
	nombre_de_sitio = get_site_name(frappe.local.site)
	ruta_archivo = '{0}/{1}'.format(str(nombre_de_sitio), str(chart_template))

	frappe.msgprint(_(ruta_archivo))
	with open(ruta_archivo, "r") as f:
		chartss = f.read()
		# frappe.msgprint(_(str(json.loads(chartss).get("tree"))))
		return json.loads(chartss).get("tree")


@frappe.whitelist()
def modify_accounts(company, chart_template=None, existing_company=None):
	template = chart_template
	try:
		delete_accounts()
	except:
		frappe.msgprint(_('No se pudieron eliminar las cuentas de la base de datos, HARD CODE'))
	else:
		create_charts(company, template, existing_company=None)


def create_charts(company, chart_template=None, existing_company=None):
	chart = get_chart(chart_template)
	if chart:
		accounts = []

		def _import_accounts(children, parent, root_type, root_account=False):
			for account_name, child in iteritems(children):
				if root_account:
					root_type = child.get("root_type")

				if account_name not in ["account_number", "account_type",
					"root_type", "is_group", "tax_rate"]:

					account_number = cstr(child.get("account_number")).strip()
					account_name, account_name_in_db = add_suffix_if_duplicate(account_name,
						account_number, accounts)

					is_group = identify_is_group(child)
					report_type = "Balance Sheet" if root_type in ["Asset", "Liability", "Equity"] \
						else "Profit and Loss"

					account = frappe.get_doc({
						"doctype": "Account",
						"account_name": account_name,
						# "company": company,
						"parent_account": parent,
						"is_group": is_group,
						"root_type": root_type,
						"report_type": report_type,
						"account_number": account_number,
						"account_type": child.get("account_type"),
						"account_currency": frappe.db.get_value('Company',  company,  "default_currency"),
						"tax_rate": child.get("tax_rate")
					})

					if root_account or frappe.local.flags.allow_unverified_charts:
						account.flags.ignore_mandatory = True

					account.flags.ignore_permissions = True

					account.insert(ignore_permissions=True)

					accounts.append(account_name_in_db)

					_import_accounts(child, account.name, root_type)

		# Rebuild NestedSet HSM tree for Account Doctype
		# after all accounts are already inserted.
		frappe.local.flags.ignore_on_update = True
		_import_accounts(chart, None, None, root_account=True)
		rebuild_tree("Account", "parent_account")
		frappe.local.flags.ignore_on_update = False


def add_suffix_if_duplicate(account_name, account_number, accounts):
	if account_number:
		account_name_in_db = unidecode(" - ".join([account_number,
			account_name.strip().lower()]))
	else:
		account_name_in_db = unidecode(account_name.strip().lower())

	if account_name_in_db in accounts:
		count = accounts.count(account_name_in_db)
		account_name = account_name + " " + cstr(count)

	return account_name, account_name_in_db


def identify_is_group(child):
	if child.get("is_group"):
		is_group = child.get("is_group")
	elif len(set(child.keys()) - set(["account_type", "root_type", "is_group", "tax_rate", "account_number"])):
		is_group = 1
	else:
		is_group = 0

	return is_group


def delete_accounts():
	frappe.db.sql('DELETE FROM `tabAccount`')
	frappe.db.commit()
