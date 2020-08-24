# -*- coding: utf-8 -*-

from odoo import models, fields, api,_ 



class hmsdoctor(models.Model):
    _name = 'hms.doctor'

    _description = "hmsDoctor"

    name = fields.Char(string='Doctor', required=True, translate=True)
    Gender_type= fields.Selection([
            ('male', 'Male'),
            ('female', 'Female'),
        ], required=True,string='Gendar')
    note = fields.Text(string='prescription'
    mobile_No = fields.Char(string= ' Mobile No.' , required = True)
    amount = fields.Float (string = 'Amount')
    
    note = fields.Text(string='prescription', translate=True) 
    doctor_name_id = fields.Many2one('hms.patient', string='Patient')

    reconciled_invoice_ids = fields.Many2many('account.move', string='Reconciled Invoices', compute='_compute_reconciled_invoice_ids', help="Invoices whose journal items have been reconciled with these payments.")
    has_invoices = fields.Boolean(compute="_compute_reconciled_invoice_ids", help="Technical field used for usability purposes")
   # move_line_ids = fields.One2many('account.move.line', 'payment_id', readonly=True, copy=False, ondelete='restrict')
   




class hmspatient(models.Model):
    _name = 'hms.patient'
    _description = "Patient"
    
    name = fields.Char(string='Patient', required=True, translate=True)
    doctor = fields.Selection([
            ('MBBS', 'MBBS'),
            ('MD', 'M_D'),

            ], required=True, string='Digree')
