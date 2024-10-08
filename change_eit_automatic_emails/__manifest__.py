# -*- coding: utf-8 -*-
{
    'name': "change_eit_automatic_emails",

    'summary': """
        send email after and befor due invoice""",

    'description': """
        add send email remainder
    """,

    'author': "merghani elfaki",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'eit_automatic_emails'],

    # always loaded
    'data': [
        'data/mail_template_data.xml',
        
        # Views
      #  'views/res_partner.xml',
    ],
}
