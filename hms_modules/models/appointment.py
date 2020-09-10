# -*- coding: utf-8 -*-

from odoo import models, fields, api,_ 
from datetime import date

class hmsappointment(models.Model):
    _name='hms.appointment'
    

    _discription = "appointment"
    
    patient = fields.Char(string='Patient',required=False)
    name = fields.Char(string='Name',required=True)
    iid=fields.Char(string='Appno')
    patient_id = fields.Many2one('hms.doctor',string='patient',required=True)
    phy_cabin_id=fields.Integer(string='Cabin No',required=False)
    app_age=fields.Char(string='Age',required=True)
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
        ('draft','Draft'),
        ('waiting','Waiting'),
        ('confirmed','Confirmed'),
        ('reject','Rejected'),
    ],string='Appointment Stage',default ='draft')
    app_reject=fields.Char(string='Reject')


    @api.model
    def create(self, vals):
       
        today = fields.Datetime.now()
    
        
        
        vals['app_date'] = today
        vals['iid'] = self.env['ir.sequence'].next_by_code('hms.appointment') or 'New'
        record =  super(hmsappointment, self).create(vals)

        return record
    def confirm_record_name(self):
        
        self.app_state="confirmed"

    def cancel_record_name(self):
        
        self.app_state="reject"
 
    
    def write(self,vals):

        app_purpose="retuned"

        if 'phy_cabin_id'in vals:
            if vals.get('phy_cabin_id'):
                app_purpose="works"
                print("uhsdic",app_purpose)
            else:
                app_purpose="    "
                print("uhsdic",app_purpose)
               
        vals['app_purpose'] = app_purpose
        record = super(hmsappointment,self).write(vals)
        return record
    
    @api.onchange('patient_id')
    def onchange_user_id(self):
     self.app_age = self.patient_id.age
