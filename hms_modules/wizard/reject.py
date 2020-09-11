# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models, _
from odoo.exceptions import UserError


class hmsreject(models.TransientModel):
	_name = "hms.reject"
	_description = "Reject"



	reason=fields.Text(string='Reason')

	
	def cancel_record_name(self):
		appointment = self.env['hms.appointment'].browse(self._context.get('active_ids', []))
		print("uhsdic",self._context.get('active_ids', []))
		appointment.app_reject=self.reason
		appointment.app_state="reject"
		
