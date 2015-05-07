# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2014 Aktiva - http://www.aktiva.com.mx
#    All Rights Reserved.
#    info Aktiva (info@aktiva.com.mx) Criesca info@criesca.com 
#    Coded by: Cristobal Escamilla (agustin.cruz@openpyme.mx)
#              Luis F. Lores Caignet (luisfqba@gmail.com)
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
    "name" : "Addenda Pepsi - Aktiva",
    "version" : "1.0",
    "author" : "Aktiva",
    "category" : "Localization/Mexico",
    "description" : """This module creates the interface for e-invoicing files from invoices with Facturalo pac.""",
    "website" : "http://www.aktiva.com.mx",
    "license" : "AGPL-3",
    "depends" : ["l10n_mx_facturae_pac_facturalo",
    ],
    "demo" : [
    ],
    "data" : [
      "invoice_view.xml",
      "res_company_view.xml",
    ],
    "test" : [
    ],
    "installable" : True,
    "active" : False,
}
