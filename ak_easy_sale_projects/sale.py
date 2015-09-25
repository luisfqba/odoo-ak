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


from osv import osv, fields
import time
from openerp.tools.translate import _

class sale_order(osv.osv):
    _name = "sale.order"
    _inherit = "sale.order"
    _columns = {
        'product_on_id':fields.many2one('product.product','Proyecto', required=False,),
        'product_qty': fields.integer('Cantidad'),
        'proyect_price': fields.float('Precio'),
        }

    _defaults = {  
        'product_qty': 1,
        }

    def on_change_load_products(self, cr, uid, ids, partner_id, product_on_id, product_qty, order_line, proyect_price, context=None):
        # pos_line_obj = self.pool.get('pos.order.line')
        product_obj = self.pool.get('product.product')
        salesman_obj = self.pool.get('res.users')
        partner_obj = self.pool.get('res.partner')
        partner = partner_obj.browse(cr, uid, partner_id, context=None)
        lines = order_line

        fpos_obj = self.pool.get('account.fiscal.position')
        fpos = partner.property_account_position.id or False
        fpos = fpos and fpos_obj.browse(cr, uid, fpos, context=context) or False
        # tax_id = [(6, 0, [_w for _w in fpos_obj.map_tax(cr, uid, fpos, product[0].taxes_id)])],

        if not product_on_id:
            return {}  
        
        qty_product = int(product_qty)

        product_id = [product_on_id]
        product_br = product_obj.browse(cr, uid, product_id, context=None)[0]
        if product_br.default_code:
            product_name = '['+product_br.default_code +']'+product_br.name
        else:
            product_name = product_br.name
        if product_id:
            #iterar por la cantidad de productos
            cant_product = 0
            while(cant_product < qty_product):                
                xline = (0,0,{
                        'product_id': product_id[0],
                        'name': product_name,
                        'tax_id': [(6, 0, [_w for _w in fpos_obj.map_tax(cr, uid, fpos, product_br.taxes_id)])],
                        'product_uom_qty': 1,
                        'price_unit': proyect_price/qty_product,
                        'product_uom': product_br.uom_id.id,    
                        'product_uos_qty': 1,
                        'state': 'draft',
                        'type' : 'make_to_stock',
                    })
                lines.append(xline)
                cant_product = cant_product + 1
        
        return {'value' : {'product_on_id':False,'order_line':[x for x in lines]}}
    
    def open_wizard_make_invoice(
        self, cr, uid, ids, fields, context=None
    ):
        '''
        This function open account statement wizard of the partner
        '''
        if context is None:
            context = {}
        # error checking
        if not ids:
            return False
        if not isinstance(ids, list):
            ids = [ids]

        # create wizard, sending partner_ids on context
        dummy, view_id = self.pool.get('ir.model.data').get_object_reference(
            cr, uid, 'ak_easy_sale_projects',
            'view_sale_order_line_make_invoice_aktiva'
        )

        return {
            'name': _("Sale order line make invoice"),
            'view_mode': 'form',
            'view_id': view_id,
            'view_type': 'form',
            'res_model': 'sale.order.line.make.invoice.aktiva',
            'type': 'ir.actions.act_window',
            'target': 'new',
        }
        
sale_order()
