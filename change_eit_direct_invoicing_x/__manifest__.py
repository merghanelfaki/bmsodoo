# -*- coding: utf-8 -*-
{
    'name': "changeeit_direct_invoicing",

    'summary': """
        Automatically creates invoices from delivery orders and includes scheduled jobs for weekly, biweekly, and monthly invoicing.
    """,

    'description': """
        This module automates the creation of invoices directly from delivery orders. 
        It includes scheduled jobs that run weekly, biweekly, and monthly to create invoices from delivery orders. 
        The module enhances efficiency by reducing manual intervention and streamlining the invoicing process.
    """,

    'author': "merghani elfaki",
    'website': "http://www.expertsintech.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0.3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'eit_direct_invoicing'],

    # always loaded
    'data': [
        # Data
        'data/direct_invoicing_data.xml',
        
        # Views
        'views/account_move.xml',
        'views/sale_order.xml',
       # 'views/res_partner.xml'
    ],
}
