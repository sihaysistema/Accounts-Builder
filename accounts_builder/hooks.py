# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "accounts_builder"
app_title = "Accounts Builder"
app_publisher = "Si Hay Sistema"
app_description = "Accounts generator"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "m.monroyc22@gmail.com"
app_license = "GNU General Public License v3.0"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/accounts_builder/css/accounts_builder.css"
# app_include_js = "/assets/accounts_builder/js/accounts_builder.js"

# include js, css files in header of web template
# web_include_css = "/assets/accounts_builder/css/accounts_builder.css"
# web_include_js = "/assets/accounts_builder/js/accounts_builder.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "accounts_builder.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "accounts_builder.install.before_install"
# after_install = "accounts_builder.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "accounts_builder.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"accounts_builder.tasks.all"
# 	],
# 	"daily": [
# 		"accounts_builder.tasks.daily"
# 	],
# 	"hourly": [
# 		"accounts_builder.tasks.hourly"
# 	],
# 	"weekly": [
# 		"accounts_builder.tasks.weekly"
# 	]
# 	"monthly": [
# 		"accounts_builder.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "accounts_builder.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "accounts_builder.event.get_events"
# }

