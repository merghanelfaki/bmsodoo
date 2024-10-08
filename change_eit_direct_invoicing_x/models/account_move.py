from odoo import models, fields, api


class AccountMoveInherit(models.Model):
    _inherit = 'account.move'

    #To be used to filter customer invoices according to the supplier's responsibility.
    responsible_Customer_id = fields.Many2one('res.users', string='Responsible Customer', related='partner_id.user_id',translate=True)

    outstanding_credits_check = fields.Boolean(compute='_compute_outstanding',string='Otstanding',
                                             help="It is valid if there are advance payments to the customer to use in the filters.",
                                             default=False , store=True)

    @api.depends('invoice_has_outstanding')
    def _compute_outstanding(self):
        for line in self:
            if line.invoice_has_outstanding==True:
                line.outstanding_credits_check=True
            else:
                line.outstanding_credits_check=False
