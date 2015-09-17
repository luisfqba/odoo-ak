# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#
#    Copyright (C) 2015-Today Aktiva Consultoria en Calidad SC (<http://www.aktiva.com>)
#    Copyright (C) 2004 OpenERP SA (<http://www.openerp.com>)
#                       All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import orm, fields
from openerp.tools.translate import _
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT

import datetime
import logging

_logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)


class wizard_download_attachments(orm.TransientModel):
    _name = "wizard.download.attachments"
    _description = 'Download invoice attachments'

    _columns = {
        'data': fields.binary("File", readonly=True),
        'name': fields.char('Filename', 32, readonly=True),
        'state': fields.selection((
            ('choose', 'choose'),   # choose
            ('get', 'get'),         # get the file
        )),
        'start_date': fields.date("Start Date", required=True),
        'end_date': fields.date("End Date", required=True),
    }

    _defaults = {
        'state': lambda *a: 'choose',
    }
       
    
    def download_attachment(self, cr, uid, ids, context={}):
        attachment_obj = self.pool['ir.attachment']
        
        #start_date
        res = self.read(cr, uid, ids, context=context)[0]
        start_date = res["start_date"] 
        #end_date
        end_date = res["end_date"]

        file_name = '{0}_to_{1}.zip'.format(str(start_date),str(end_date))        
        query_sql2 = "(select id from account_invoice where date_invoice >=  '"+str(start_date)+"' and date_invoice <= '"+str(end_date)+"')"
        query_sql ="""select file_xml_sign, file_pdf 
                    from ir_attachment_facturae_mx  
                    where state='done' 
                    and invoice_id in """+ query_sql2
                    
                
        cr.execute(query_sql)        
        lines = cr.dictfetchall()
        
        attachment_ids = set()
        for attachment in lines:
            attachment_ids = attachment_ids.union(attachment_obj.search(cr, uid, [('id', '=', attachment['file_xml_sign']),
                                                                                  ], context=context))
            attachment_ids = attachment_ids.union(attachment_obj.search(cr, uid, [('id', '=', attachment['file_pdf']),
                                                                                  ], context=context))
        out = attachment_obj.get_as_zip(cr, uid, attachment_ids, log=True)
        self.write(cr, uid, ids, {'state': 'get', 'data': out, 'name': file_name}, context=context)
        return {
            'type': 'ir.actions.act_window',
            'name': "Download Done",
            'res_model': 'wizard.download.attachments',
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': self.browse(cr, uid, ids)[0].id,
            'views': [(False, 'form')],
            'target': 'new',
        }