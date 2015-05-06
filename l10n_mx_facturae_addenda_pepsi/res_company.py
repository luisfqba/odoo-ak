# -*- encoding: utf-8 -*-

from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp import pooler, tools

class res_company(osv.Model):
    _inherit = 'res.company'

    _columns = {
        'addenda_pepsi_idproveedor' : fields.char('Codigo de Proveedor', size=30, help='Codigo del proveedor para la addenda de Pepsi'),
    }
