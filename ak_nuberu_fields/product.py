from openerp.osv import osv, fields
from warnings import catch_warnings


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
        'rate_price_supllier': fields.function(get_rate_price_supllier, type='float', method=True, string='Precio Tarifa Unitario'),
    }

product_product()
