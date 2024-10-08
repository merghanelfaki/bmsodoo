# -*- coding: utf-8 -*-
from decorator import append

from odoo import models, fields, api
from datetime import date, datetime, timedelta
import base64

from odoo.addons.purchase.models.res_partner import res_partner


class AccountMove(models.Model):
    _inherit = 'account.move'
    
    def send_mail(self, email_template,email_values):
        sent_to_emails = [x.name for x in self.partner_id.sent_to_emails]
       # print("------------------sent_to_emails",sent_to_emails)
        email_values = {}
        print("--------------email_values-1-------",email_values)
        email_values['email_to'] = ', '.join(sent_to_emails)

        print("--------------email_values-2-------",email_values)

        email_template.sudo().with_context(
            email_from= 'e-inv@bm.com.sa',
            email_to=self.partner_id.email,
        ).send_mail(self.id, email_values=email_values, force_send=True)
    
    def partner_invoices(self):
        account_moves = self.env['account.move'].search([
            ('payment_state', '=', 'not_paid'), ('state', 'in', ['posted'])
        ]).filtered(lambda x: x.partner_id.enabled_invoice_notification)
        

      #  print("acountmove------------",account_moves)
        email_template = ''
        for move in account_moves:

          #  print("acountmove--------for----", account_moves)
            current_date = date.today()
            if move.invoice_date_due:
              #  print("dddddddddddddddddddddddddd")
                # Calculate the difference between due date and current date
                difference = move.invoice_date_due - current_date
               # print("adifference----------------------",difference)
                # Check the difference and categorize the invoice due date
                #if difference.days < 0:
                  #  continue
                #if difference.days == 0 or difference.days < 3 :
                 #  continue
                if difference.days ==5 or  difference.days == 3:

                    print("five days-------------",difference.days)
                    email_template = self.env.ref('change_eit_automatic_emails.eit_payment_reminder_template_befor_five_days')
                if difference.days ==0:
                    print("zeroooooooooooooooo",difference.days)
                    email_template = self.env.ref('change_eit_automatic_emails.eit_payment_reminder_template_zer_days')
                if difference.days <=-2 or difference.days == -9 and difference.days <= -30 :
                    print("------------------------------------------")
                    email_template = self.env.ref('change_eit_automatic_emails.eit_payment_reminder_template_after_21_days')


                if email_template:
                    print("ddddddddddddddddddddddddddddddddddd")
                    move.send_mail(email_template,account_moves)
                    print("ddddddddddddddddddddddddddddddddsssssddddddd")



                