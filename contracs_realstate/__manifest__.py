{
    'name': 'Conracts Bluding',
    'depends': ['base','account','hr'],
    'author': 'merghani elfaki ',
    'description': """ This module Conracts Bluding""",
    'data': [
             'security/security.xml',
             'security/ir.model.access.csv',
              'data/demo_data.xml',
              'data/remindercron_contract_paid.xml',
             'views/configuration_views.xml',

             ],

    # ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}
