# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014-2015 AKTIVA S.A. (<http://www.aktiva.com.mx>).
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

from openerp.osv import fields, osv

class ak_mrp_production_sequence(osv.Model):
    _inherit = 'mrp.production'
    
    _columns ={
        'name': fields.char('Reference', size=64),
        }
    
    _defaults = {
        'name': '',
        }
    
    def create(self, cr, uid, vals, context=None):  
        if not 'name' in vals:
            sequence  = self.pool.get('ir.sequence').get(cr, uid, 'mrp.production', context=context) or '/'
            vals['name'] = sequence
        res = super(ak_mrp_production_sequence, self).create(cr, uid, vals, context=context)
        return res

