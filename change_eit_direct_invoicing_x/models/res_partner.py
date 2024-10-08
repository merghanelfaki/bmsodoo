from odoo import models, fields, api


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'
    #add only 72_hours
    transfer_duration_type = fields.Selection([
        ('direct', 'Direct'),
        ('weekly', 'Weekly'),
        ('biweekly', 'BiWeekly'),
        ('monthly', 'Monthly'),
        ('24_hours', '24 Hours'),  # add new by merghani
        ('48_hours', '48 Hours'),
        ('72_hours', '72 Hours')
    ], default='direct', string="Transfer Invoice Duration")