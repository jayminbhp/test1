# -*- coding: utf-8 -*-

from odoo import models, fields, api,_ 


class hmsappointmentextention(models.Model):
    _inherit='hms.appointment'
    
    surname=fields.Char(string='Surname')