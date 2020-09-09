# -*- coding: utf-8 -*-
from odoo import models, fields, api,_ 



class hmsprescription(models.Model):
    _name = 'hms.prescription'

    _description = "prescription"



    name=fields.Char(string='Patient Name')
    patient_id = fields.Char(string='Patient Id')
    prescribed_doctor=fields.Many2one('prescribed.doctor',string='Prescribed Doctor')
    disease=fields.Many2one('prescribed.patient',string='Disease')
    prescription_date=fields.Datetime(string='date',required=False)
    medicament=fields.Many2one('medicament.group',string='Medicament Group')


class medicamentgroup(models.Model):
	_name='medicament.group'

	_description="medicamentgroup"


	name=fields.Char(string='Doctor name',required=True)
	limit=fields.Float(string='Limit')


class prescribeddoctor(models.Model):
	_name='prescribed.doctor'

	_description="prescribeddoctor"

	name=fields.Char(string='Doctor Name',required=True)
	physician_type= fields.Selection([
            ('physician', 'Physician'),
            ('cardiologist','Cardiologist'),
            ('physiotherapist','physiotherapist'),
            ('dentel','Dentel'),
            ('gynec','Gynec'),
        ], required=True,string='Physician Type')


class prescribedpatient(models.Model):
	_name='prescribed.patient'

	_description="prescribedpatient"

	name=fields.Char(string='Patient Id',required=True)
	disease_type= fields.Char(string='disease')
	

