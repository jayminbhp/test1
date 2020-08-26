# -*- coding: utf-8 -*-

from odoo import models, fields, api,_ 
from datetime import date

class hmsappointment(models.Model):
    _name='hms.appointment'
    

    _discription = "appointment"
    
    patient = fields.Char(string='Patient',required=False)

    patient_id = fields.Many2one('hms.doctor',string='patient',required=True)
    phy_cabin_id=fields.Integer(string='Cabin No',required=False)
    app_date=fields.Datetime(string='date',required=False)
    app_urgency_level=fields.Selection([
            ('urgent','Urgent'),
            ('critical','Critical'),
            ('normal','Normal') ,
            ],required = False,string='Urgency level')
    app_purpose=fields.Char(string='Purpose',required=False)
    app_complain=fields.Char(string='Chif complain',required=False)
    app_responsible_jr_doc=fields.Char(string='Responsible junior doctor',required=False)
    app_chief_comp=fields.Char(string='Chief Complain',required=False)
    app_history_illness=fields.Char(string='History of Illness',required=False)
    app_past_hisory=fields.Char(string='Past History')
    app_state=fields.Selection([
        ('waiting','Waiting'),
        ('confirmed','Confirmed'),
    ],string='Appointment Stage')
    @api.model
    def create(self, vals):
       
        today = fields.Datetime.now()
       
        
        vals['app_date'] = today
        record =  super(hmsappointment, self).create(vals)
        return record

    # @api.model
    # def create(self, vals):
    #     # app_date = vals.get('app_date', '')
    #     # if app_date:
    #     #vals['app_date'] = self.(app_date, vals.get('app_date'))
        
    #     #from datetime import date
    #     #today = date.today()
    #     #return super(hmsappointment, self).create(vals[{'today','today'}]   )
    #     print 'Fields and their values to be created in a dictionary',vals
    #     res = super(res_users, self).create(vals)

    #     return res

