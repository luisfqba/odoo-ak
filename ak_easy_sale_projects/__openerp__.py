# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Authors: Aktiva (<http://www.aktiva.com.mx>)
#    Planified by: Arturo Rubio
#    Audited by: Arturo Rubio
#
#    Coded by: Luis Felipe Lores Caignet (luisfqba@gmail.com)
#              german_442 email: (german.ponce@hesatecnica.com)
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
    'name': 'Ventas y Facturacion Aktiva',
    'version': '1.0',
    "author" : "PonceSoft, Luis F. Lores Caignet(luisfqba@gmail.com)",
    "category" : "Sales",
    'description': """
    
    VENTAS Y FACTURACION AKTIVA:
    
    Modulo que permite Crear Cotizaciones de Proyectos de Forma Rapida solo Agregando la Cantidad y el Producto.
    
    Funciona para Ventas.

    Funcionamiento:
        -En el Formulario de Pedido antes del Apartado de Lineas, existen 2 Campos, Cantidad y Producto. Al seleccionar el Producto se agregara la linea de Forma Automatica, tomando como referencia principal los detalles de la Ficha del Producto.

    """,
    "website" : "http://www.aktiva.com.mx",
    "license" : "AGPL-3",
    "depends" : ["account","sale"],
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : [
                    "sale_view.xml",
                    'wizard/sale_line_invoice.xml',
                    #'security/ir.model.access.csv',
                    ],
    "installable" : True,
    "active" : False,
}
