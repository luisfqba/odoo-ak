# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2013 OpenPyme - http://www.openpyme.mx
#    All Rights Reserved.
#    info OpenPyme (info@openpyme.mx)
#    Coded by: Agustín Cruz (agustin.cruz@openpyme.mx)
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

import re
import logging
import string
import base64

from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp import tools

logger = logging.getLogger(__name__)

try:
    from SOAPpy import WSDL
except:
    logger.error("Package SOAPpy missed")


class ir_attachment_facturae_mx(osv.Model):
    _inherit = 'ir.attachment.facturae.mx'

    def sign_file(self, cr, uid, ids, fdata=None, context=None):
        dicc_signed = super(ir_attachment_facturae_mx, self).sign_file(cr, uid, ids,fdata=fdata, context=context)        
        invoice = None
        for attachment in self.browse(cr, uid, ids, context=context):
            invoice = attachment.invoice_id
        try:
            invoice.addenda_pepsi            
        except NameError:
            #do nosthing
            pass
        else:
            if invoice.addenda_pepsi:
                cfdi_xml = dicc_signed['cfdi_xml']
                dicc_signed['cfdi_xml'] = cfdi_xml.replace('</cfdi:Complemento>', 
                    '</cfdi:Complemento><cfdi:Addenda><RequestCFD tipo="AddendaPCO" version="2.0" idPedido="' + invoice.addenda_pepsi_idpedido
                    + '"><Documento folioUUID="' + re.search('UUID="([\S\s]{36})', cfdi_xml).group(1)
                    + '" tipoDoc="1"/><Proveedor idProveedor="' + invoice.company_emitter_id.addenda_pepsi_idproveedor
                    + '"/><Recepciones><Recepcion idRecepcion="' + invoice.addenda_pepsi_idrecepcion 
                    + '">' + re.search('<cfdi:Conceptos>([\S\s]*)</cfdi:Conceptos>', cfdi_xml).group(1)
                    + '</Recepcion></Recepciones></RequestCFD></cfdi:Addenda>')              
        return dicc_signed

    