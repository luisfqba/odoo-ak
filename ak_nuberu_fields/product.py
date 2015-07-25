from openerp.osv import osv, fields

class product_product(osv.Model):
    _name = 'product.product'
    _inherit = 'product.product'

    def get_rate_price_supllier(self, cr, uid, ids, name, args, context=None):
        """Funcion que muestra el precio unitario del primer proveedor del producto"""
        res = {}
        if not ids: return result
        result = 0.0
        for record in self.browse(cr, uid, ids, context=context):
            try:
                result = record.seller_ids[0].pricelist_ids[0]['price']
            except:
                pass
            res[record.id] = result
        return res


    _columns = {
        'rate_price_supllier': fields.function(get_rate_price_supllier, type='float', method=True, string='Precio Unitario Proveedor'),
    }

    def write(self, cr, uid, ids, vals, context=None):
        product_obj=self.pool.get('product.product')
        new_product_obj=product_obj.browse(cr, uid, ids[0], context=context)
        all_groups=self.pool.get('res.groups')
        edit_group = all_groups.browse(cr, uid, all_groups.search(cr,uid,[('name','=','Producto solo lectura')])[0])
        groups_users=edit_group.users
        for groups_user in groups_users:
            if uid == groups_user.id:
                raise osv.except_osv('Warning!',"Usted no tiene permiso para Modificar/Crear productos!")
            else:
                return super(product_product, self).write(cr, uid, ids, vals, context = context)
        return super(product_product, self).write(cr, uid, ids, vals, context = context)
    
    def unlink(self, cr, uid, ids, context=None):
        product_obj=self.pool.get('product.product')
        new_product_obj=product_obj.browse(cr, uid, ids[0], context=context)
        all_groups=self.pool.get('res.groups')
        edit_group = all_groups.browse(cr, uid, all_groups.search(cr,uid,[('name','=','Producto solo lectura')])[0])
        groups_users=edit_group.users
        for groups_user in groups_users:
            if uid == groups_user.id:
                raise osv.except_osv('Warning!',"Usted no tiene permiso para Eliminar productos!")
            else:
                return super(product_product, self).unlink(cr, uid, ids, context = context)
        return super(product_product, self).unlink(cr, uid, ids, context = context)
    
    def copy(self, cr, uid, id, default=None, context=None):
        product_obj=self.pool.get('product.product')
        new_product_obj=product_obj.browse(cr, uid, id, context=context)
        all_groups=self.pool.get('res.groups')
        edit_group = all_groups.browse(cr, uid, all_groups.search(cr,uid,[('name','=','Producto solo lectura')])[0])
        groups_users=edit_group.users
        for groups_user in groups_users:
            if uid == groups_user.id:
                raise osv.except_osv('Warning!',"Usted no tiene permiso para Duplicar productos!")
            else:
                return super(product_product, self).copy(cr, uid, id, default=default, context = context)
        return super(product_product, self).copy(cr, uid, id, default=default, context = context)