# -*- coding: utf-8 -*-
# from odoo import http


# class Pruebaversiones(http.Controller):
#     @http.route('/pruebaversiones/pruebaversiones', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pruebaversiones/pruebaversiones/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pruebaversiones.listing', {
#             'root': '/pruebaversiones/pruebaversiones',
#             'objects': http.request.env['pruebaversiones.pruebaversiones'].search([]),
#         })

#     @http.route('/pruebaversiones/pruebaversiones/objects/<model("pruebaversiones.pruebaversiones"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pruebaversiones.object', {
#             'object': obj
#         })

