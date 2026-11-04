# -*- coding: utf-8 -*-
{
    'name': "Hospital Manager",
    'summary': "Product for hospitals and patients",
    'description': """
          using this module for complete manage your hospital and get good reports 
    """,
    'author': "alMohamady",
    'website': "https://www.alMohamady.com",
    'category': 'Uncategorized',
    'version': '0.1.1',

    'depends': [
        'base',
        'mail',
        'stock',
        'product',
        'sale',
        'purchase',
        'account',
        'point_of_sale',
        'crm',
        'hr',
    ],

    'assets': {
        'web.assets_backend': [
            'my_hospital/static/src/scss/rtl.scss',
        ],
    },

    'data': [
        'security/ir.model.access.csv',
        'views/employee_view.xml',
        'views/doctors.xml',
        'data/sequences.xml',
        'security/security.xml',
        'wizards/add_appointment.xml',
        'views/patients.xml',
        'views/appointments.xml',
        'views/prescription_views.xml',
        'views/product_template_views.xml',
        'views/menus.xml',
    ],
}