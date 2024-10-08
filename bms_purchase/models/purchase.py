from odoo import models, fields, api, _
from itertools import groupby
from odoo.exceptions import AccessError
from odoo.fields import Many2one


#
class PurchaseOrderInherit(models.Model):
    _inherit = 'purchase.order'
    purchase_type = fields.Selection([
        ('production', 'Production'),
        ('maintenance', 'maintenance')
    ], string="Purchase Type" , default='production')
    requested_by = Many2one('hr.employee' , string="Requested By")

    driver_id = Many2one('hr.employee' , string="Driver Name")

    operating_unit_d = Many2one('operating.unit' , string="Operating Unit")
    model_id = Many2one('fleet.vehicle' , string="Model")
    #driver_id1 = Many2one('res_partner' , string="Driver Name" ,translate=True )
    license_plate = fields.Char(string="license",related='model_id.license_plate',translate=True)
    model_year = fields.Char(string="Model Year", related='model_id.model_year' ,translate=True, default='001294', readonly=1)
    no_iso = fields.Char(string="NO",translate=True , default='001294' ,readonly=1)
    remark = fields.Text(string="Remark",translate=True )







