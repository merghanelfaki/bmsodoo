# -*- coding: utf-8 -*-

{
    'name': "Purchase Manitanence",

    'summary': """
       Adds Purchase Manitanence type
    """,

    'author': "merghani",
    'website': "http://www.bms.com.sa",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase','hr_fleet',],

    # always loaded
    'data': [
        'views/purchase.xml',
        'report/purchase_reports.xml',
        'report/purchase_order_templates.xml',
        'report/purchase_quotation_templates.xml',


    ],
}
