from odoo import models, fields, api, _
from odoo.tools import UserError
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class StockPickingInherit(models.Model):
    _inherit = 'stock.picking'
    #In this function, a condition of the last three days to send the invoice has been added.
    def partner_scheduled_invoicing(self, cron_policy):

        end_date = datetime.now()
        if cron_policy == 'weekly':
            start_date = end_date - timedelta(days=7)
        
        if cron_policy == 'biweekly':
            start_date = end_date - timedelta(days=14)
            
        if cron_policy == 'monthly':
            start_date = end_date - relativedelta(months=1)
        ##add by merghani to 72 hours  hours

        if cron_policy == '24_hours':
            start_date = end_date - timedelta(days=1)

        if cron_policy == '48_hours':
            start_date = end_date - timedelta(days=2)

        if cron_policy == '72_hours':
            start_date = end_date - timedelta(days=3)
        pickings = self.env['stock.picking'].search([
            '&', '&', ('date_done', '>=', start_date.strftime('%Y-%m-%d 00:00:00')),
            ('date_done', '<=', end_date.strftime('%Y-%m-%d 23:59:59')),
            '|', ('invoice_created', '=', False), ('invoice_created', '=', None)
        ]).filtered(lambda x: x.picking_type_id.code == 'outgoing')


        self.create_invoices(pickings, cron_policy)
