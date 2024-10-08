from odoo import models, fields, api, _
from itertools import groupby
from odoo.exceptions import AccessError

#
class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
    #add only 72_24_48_hours
    transfer_duration_type = fields.Selection([
        ('direct', 'Direct'),
        ('weekly', 'Weekly'),
        ('biweekly', 'BiWeekly'),
        ('monthly', 'Monthly'),
        ('24_hours', '24 Hours'),  #add new by merghani
        ('48_hours', '48 Hours'),
        ('72_hours', '72 Hours')
    ], string="Transfer Invoice Duration")
