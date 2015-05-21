# -*- encoding: utf-8 -*-

from openerp.osv import fields, osv

class account_invoice(osv.Model):
    _inherit = 'account.invoice'

    _columns = {
        'num_fact_proyecto': fields.char('Factura', size=10, help='Numero de factura del total de Proyecto'),
    }