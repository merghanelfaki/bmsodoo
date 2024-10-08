# -*- coding: utf-8 -*-
# from odoo import http


# class BmsInvoice(http.Controller):
#     @http.route('/bms_invoice/bms_invoice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bms_invoice/bms_invoice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bms_invoice.listing', {
#             'root': '/bms_invoice/bms_invoice',
#             'objects': http.request.env['bms_invoice.bms_invoice'].search([]),
#         })

#     @http.route('/bms_invoice/bms_invoice/objects/<model("bms_invoice.bms_invoice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bms_invoice.object', {
#             'object': obj
#         })
