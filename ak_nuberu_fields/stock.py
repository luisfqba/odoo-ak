# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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

from openerp.osv import orm, fields

# ----------------------------------------------------
# Incoveniente al cambiar la Categoria del Producto debido a que
# en stock_move se almacena tiene que guardar la Categoria
# implementar luego funcionalidad para actualizar la Categoria almacenada
# ----------------------------------------------------

class stock_move(orm.Model):
    _inherit = "stock.move"
    _columns = {
        'categ_id': fields.related('product_id','categ_id','name',type='char', relation="product.product", string="Categoria Producto", store=True),
    }

class stock_picking(orm.Model):
    _inherit = 'stock.picking'
    _columns = {
        'client_order_ref': fields.related('sale_id','client_order_ref',type='char', relation='sale.order',
                                   string='Refencia del Cliente'),
    }

class stock_picking_out(orm.Model):
    _inherit = 'stock.picking.out'
    
    _columns = {
        'client_order_ref': fields.related('sale_id','client_order_ref',type='char', relation='sale.order',
                                   string='Refencia Cliente'),          

    }
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
