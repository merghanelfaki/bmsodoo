""""
This file represents configuration models for the module
Author: MASAD - HQ
"""
from odoo import models, fields
from odoo import models, fields, api, _
from datetime import date, datetime, timedelta

from odoo.tools import translate


########################################################################################################################
class Buildingdetails(models.Model):
    _name = 'building.details'
    _description = 'Building Name'

    name = fields.Char(string='Building Name',translate=True)
    type_building = fields.Char(string='Type Of Building',translate=True)
    number_floors = fields.Integer(string='Number of floors' )
    number_elevators = fields.Char(string='Number of elevators',translate=True)
    number_units = fields.Integer(string='Number Of Units')
    number_parking = fields.Integer(string='Number Parking' )
    property_usage = fields.Selection(string='property usage',selection=[
        ('family_housing', 'Family housing'), ('factories', 'Factories'),
        ('companies', 'Companies'),('Warehouses', 'Warehouses'),
        ('parking ', 'Parking')
    ], default='family_housing',translate=True)

    class scheduledPayment(models.Model):
        _name = 'scheduled.payment'
        _description = 'scheduledPayment'

        # DATA CONTRACT 1 ###3
        no_invoice = fields.Char(string='No Invoice')
        name = fields.Many2one('contracts.building', string='NO Contract')
        building_name = fields.Many2one('building.details',related='name.building_name',string='Building Name')
        start_date = fields.Date(string='Tenacy Star Date',related='name.start_date')
        end_date = fields.Date(string='Tenacy End Date',related='name.start_date')
        start_date = fields.Date(string='Tenacy Star Date',related='name.start_date')
        payment_date = fields.Date(string='Payment Date')

        # DATA CONTRACT 1 ###3
        total_contract_value = fields.Float(string='Total Contract Value',related='name.total_contract_value')
        requaler_rent_payment = fields.Float(string='Requaler Rent Payment',related='name.requaler_rent_payment')
        analytic_account_id = fields.Many2one('account.analytic.account', string='Analytic Account',related='name.analytic_account_id')
        state = fields.Selection([
            ('not_paid', ' Not Paid'),('paid', 'Paid')
        ], string='Status', readonly=True, default='not_paid')
        rent_pay_cycle = fields.Selection(string='Rent Payment Cycle', selection=[
            ('monthly', 'Monthly'), ('2_month', 'Tow Month'),
            ('half', 'Half'), ('quarterly', 'Quarterly'), ('annually', 'annually'),

        ], default='quarterly', translate=True,related='name.rent_pay_cycle')
        contractsbuilding_id= fields.Many2one('contracts.building' ,string='contracts building')

        employee_id = fields.Many2one('hr.employee', string='Employee Name')

        def send_mail(self, email_template):
            sent_to_emails = [x for x in self.employee_id.work_email]
            # print("------------------sent_to_emails",sent_to_emails)
            email_values = {}
            print("--------------email_values-1-------", email_values)
            email_values['email_to'] = ', '.join(sent_to_emails)
            email_values = {}
            print("--------------email_values-2-------", email_values)
            email_template.sudo().with_context(
                email_from='e-inv@bm.com.sa',
                email_to=self.employee_id.work_email,
            ).send_mail(self.id, email_values=email_values, force_send=True)
            print("eeeeeeeeeeeeeeemail_templateemail_templateeeeeeeeeeeeeeee",email_template)

        def partner_contrcat(self):
            scheduledpaid = self.env['scheduled.payment'].search([
                ('state', '=', 'not_paid')
            ])
            email_template = ''
            for move in scheduledpaid:
                current_date = date.today()
                if move.payment_date:
                        difference = move.payment_date - current_date
                        print("ddddddddddddddddd",difference)
                        print("dddddddddstateeeeedddddddd",move.state)
                        if difference.days ==30  or difference.days ==20and move.state =='not_paid':
                            email_template = self.env.ref('contracs_realstate.eit_contract_scheduled_paymentl_befor_due')

                        if difference.days ==0 and move.state =='not_paid':
                            email_template = self.env.ref('contracs_realstate.eit_contract_scheduled_paymentl_due_date')

                        if difference.days > 0 and move.state =='not_paid':
                            print("-------s---------------",move.state)
                            email_template = self.env.ref('contracs_realstate.eit_contract_scheduled_paymentl_after_due_date')

                        if email_template:
                             print("ddddddddddddddddddddddddddddddddddd")
                             move.send_mail(email_template)

        def sent_paid(self):
            self.write({'state': 'paid'})
            return True

        def sent_notpaid(self):
            self.write({'state': 'not_paid'})

class ContractsBuilding(models.Model):
    _name = 'contracts.building'
    _description = 'ContractsBuilding'

     #DATA CONTRACT 1 ###3
    name = fields.Char(string='No Contract')
    building_name = fields.Many2one('building.details',string='Building Name')
    contract_sealigdate = fields.Date(string='Contract Sealing Dtae')
    start_date = fields.Date(string='Tenacy Star Date')
    end_date = fields.Date(string='Tenacy End Date')
    Contract_location = fields.Char(string='Contract Sealing Location')
    contract_type = fields.Selection(string='Contrcat Type', selection=[
    ('new', 'NEW'), ('update', 'Update')
        ], default='new')
        # DATA CONTRACT 1 ###3
    analytic_account_id = fields.Many2one('account.analytic.account', string='Analytic Account')
    total_contract_value =fields.Float(string='Total Contract Value')
    requaler_rent_payment = fields.Float(string='Requaler Rent Payment',compute='_compute_amount',store=True)

    state = fields.Selection([
            ('new', 'NEW'),
            ('run', 'Runig'),
            ('end', 'End'),
            ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, default='new')
    rent_pay_cycle = fields.Selection(string='Rent Payment Cycle', selection=[
            ('monthly', 'Monthly'), ('2_month', 'Tow Month'),
            ('half', 'Half'),('quarterly','Quarterly'),('annually', 'annually'),
        ], default='quarterly', translate=True)

    scheduled_payment_ids= fields.One2many('scheduled.payment','contractsbuilding_id',String='Payment')
    def sent_run(self):
        self.write({'state': 'run'})
        return True
    def sent_end(self):
        self.write({'state': 'end'})
        return True
    def sent_cancel(self):
        self.write({'state': 'cancel'})
        return True
    def sent_new(self):
        self.write({'state': 'new'})
        return True

    @api.depends('rent_pay_cycle','total_contract_value')
    def _compute_amount(self):
        for line in self:
            if line.total_contract_value:
               if line.rent_pay_cycle== 'monthly':
                    line.requaler_rent_payment = (line.total_contract_value/12)
               if line.rent_pay_cycle == '2_month':
                    line.requaler_rent_payment = (line.total_contract_value/6)
               if line.rent_pay_cycle == 'half':
                    line.requaler_rent_payment = (line.total_contract_value/2)
               if line.rent_pay_cycle == 'quarterly':
                    line.requaler_rent_payment = (line.total_contract_value/4)
               if line.rent_pay_cycle == 'annually':
                    line.requaler_rent_payment = line.total_contract_value

    def create_scheduled(self):

        payment = self.env['scheduled.payment']

        print("--------------dd------------", self.id)
        count = 0
        for line in self:


                print("------------1----------",line.building_name,line.name)
                print("-----------2-----------",line.start_date,line.building_name.id)
                print("------------3----------",line.end_date)
                print("----------4------------",line.total_contract_value)
                print("-----------5-----------",line.requaler_rent_payment)
                print("------------6----------",line.rent_pay_cycle)
                print("------------7--------------",line.id)
                if line.rent_pay_cycle == 'monthly':
                    if count <12 :
                        print("aaaaaaaaaaaaa",count)
                        payment.create({
                                        'name': line.id,
                                        'building_name':line.building_name,
                                        'start_date': line.start_date,
                                        'end_date': line.end_date,
                                        'total_contract_value': line.total_contract_value,
                                        'requaler_rent_payment': line.requaler_rent_payment,
                                        'rent_pay_cycle': line.rent_pay_cycle,
                                        'rent_pay_cycle':line.rent_pay_cycle,
                                        'rent_pay_cycle':line.rent_pay_cycle,
                                        'contractsbuilding_id': self.id})
                        count = count + 1

                        print("cccccccccccccccc",count)
