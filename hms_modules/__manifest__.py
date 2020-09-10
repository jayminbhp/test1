# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'hospital',
    'version': '1.1',
    'category': 'business',
    'summary': 'hospital Management system',
    'description': """
This module contains all the common features of hospial management system and hendling.
    """,
    'depends': ['base'],
    'data': [
    'security/ir.model.access.csv',

    'wizard/reject.xml',

    'view/view.xml',
    'view/appointment.xml',
    'view/physician.xml',
    'view/prescription.xml',
    'data/ir_sequence_data.xml'



    


    ],
    'demo': [
        
    ],
    'qweb': [
        
    ],
    'installable': True,
    'auto_install': False
}
