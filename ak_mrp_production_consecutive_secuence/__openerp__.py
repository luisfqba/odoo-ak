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
{
    'name': 'Ak MRP production consecutive sequence',
    'version': '1.0',
    'author': 'Aktiva',
    "website" : "http://www.aktiva.com.mx",
    "license" : "AGPL-3",
    'category': 'mrp',
    'description': """This module amend the Sequence of Production Order when this is Create/Confirm.
    """,
    'update_xml': ['mrp_view.xml'],
    'depends': ['mrp',],
    'init_xml': [],
    'demo_xml': [],
    'license': 'AGPL-3',
    'installable': True,
    'active': False,
}
