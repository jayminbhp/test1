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
		# vals="details"

		# if 'reject'in vals:
		# 	if vals.get('app_reject'):
		# 		app_reject="works"
		# 		print("uhsdic",app_reject)
		# 	else:
		# 		app_reject="    "
				

		# print("uhsdic",app_reject)
			   
		# vals['app_reject'] = app_reject
		# record = super(hmsappointment,self).write(vals)
		# return record
