// Copyright (c) 2019, Si Hay Sistema and contributors
// For license information, please see license.txt

frappe.ui.form.on('Account Builder', {
	refresh: function(frm) {

	},
	insertar_data: function(frm){
		frappe.call({
			method: "accounts_builder.utils.modify_accounts",
			args: {
				company: frm.doc.compania,
				chart_template: frm.doc.upload_json
			},
			callback: function () {
				// frm.reload_doc();
			}
		});
		console.log(frm.doc.compania)
	}
});
