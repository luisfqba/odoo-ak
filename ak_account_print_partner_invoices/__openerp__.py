# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Authors: Aktiva (<http://www.aktiva.com.mx/>)
#             
#    Coded by: Luis Felipe Lores Caignet (luisfqba@gmail.com  llores@aktiva.com.mx)
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

{
    "name": "Creacion de Reporte Estado Facturas Cliente",
    "version": "1.0.0",
    "author": "Aktiva",
    "category": "Localization/Mexico",
    "description": """
    This module create PDF report with Account Invoice Status.
    """,
    "website": "http://www.aktiva.com.mx/",
    "license": "AGPL-3",
    "depends": [
        "account",
        "document",
        'report_webkit',
        "l10n_mx_facturae",
    ],
    "update_xml": [
        'report/account_print_invoices.xml'
    ],
    "installable": True,
}
