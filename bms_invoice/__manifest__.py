# -*- coding: utf-8 -*-
{
    'name': "bms_invoice",
    'summary': "Standard Invoice Template",
    'author': "Saleh Ali",
    'website': "http://www.bm.com.sa",
    'category': 'Extra Tools',
    'version': '1.1',
    'depends': [
        'account',
        'operating_unit',
        'sale_operating_unit'
    ],
    'data': [
        'reports/custom_header_footer.xml',
        'reports/bms_invoice_paper_format.xml',
        'reports/invoice.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'assets': {
        'web.report_assets_common': [
            'bms_invoice/static/src/less/fonts.less'
        ]
    },
}