# -*- encoding: utf-8 -*-

from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp import pooler, tools
from openerp import netsvc, release

class account_invoice(osv.Model):
    _inherit = 'account.invoice'

    _columns = {
        'addenda_pepsi': fields.boolean('Agregar addenda pepsi', help='Marcar esta casilla para generar el XML con la addenda de Pepsi'),
        'addenda_pepsi_idpedido': fields.char('Codigo de Pedido', size=30, help='Codigo de Pedido para la addenda de Pepsi'),
        'addenda_pepsi_idrecepcion': fields.char('Codigo de Recepcion', size=30, help='Codigo de Recepcion para la addenda de Pepsi'),
    }
