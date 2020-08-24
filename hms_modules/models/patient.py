
# -*- coding: utf-8 -*-

from odoo import models, fields, api,_ 



class hmspatient(models.Model):
    _name = 'hms.patient'

    _description = "Patient"

    name = fields.Char(string='Patient',required=True)
    mobile = fields.Char(string='Mobile',required=True)
    amount_id = fields.Float(string='Amount',required=False)
    patient_type= fields.Selection([
            ('male', 'Male'),
            ('female', 'female'),
            
        ], required=False,string='Gender')
    patient_code=fields.Char(string='Identificatin code',required=False)
    note = fields.Text(string='Description', translate=True) 
    patient_name_id = fields.Many2one('hms.doctor', string='Doctor')

    patient_pic = fields.Image("patient pic", max_width=1920, max_height=1920)

    reconciled_invoice_ids = fields.Many2many('account.move', string='Reconciled Invoices', compute='_compute_reconciled_invoice_ids', help="Invoices whose journal items have been reconciled with these payments.")
    has_invoices = fields.Boolean(compute="_compute_reconciled_invoice_ids", help="Technical field used for usability purposes")
    patient_add = fields.Text(string="Address",translate=True)
    E_mail_Id=fields.Char(string="E_mail_Id",required=True)
    Date_of_Birth=fields.Date(string="Date_of_Birth",required=True)
    online_booking=fields.Boolean(string="Online Booking Done",required=True)
    #move_line_ids = fields.One2many('account.move.line', 'payment_id', readonly=True, copy=False, ondelete='restrict')
    move_reconciled = fields.Boolean(compute="_get_move_reconciled", readonly=True)
    doc_name = fields.One2many('hms.doctor', 'doctor_name')
    














class hmsdoctor(models.Model):
    _name = 'hms.doctor'
    _description = "doctor"

    name = fields.Char(string='doctor',required=True)
    patient = fields.Selection([
            ('MBBS', 'MBBS'),
            ('MD', 'M_D'),

            ], required=True, string='Digree')
    doctor_name=fields.Char(string="Department")