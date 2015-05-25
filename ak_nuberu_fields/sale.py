# -*- encoding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################

from openerp.osv import osv, fields

class sale_order_line(osv.Model):
    _inherit = 'sale.order.line'
    _columns = {
        'ref_partner_nu': fields.char('Referencia Cliente', size=50),
        }
"""
class sale_order(osv.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'

    def _prepare_order_line_move(self, cr, uid, order, line, picking_id, date_planned, context=None):
        res = super(sale_order, self)._prepare_order_line_move(cr, uid, order=order, line=line, picking_id=picking_id, date_planned=date_planned, context=context)
        res['ref_partner_nu'] = line.ref_partner_nu
        return res
"""