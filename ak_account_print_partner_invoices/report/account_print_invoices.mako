<html>
    <head>
        <style type="text/css">
            ${css}
        </style>
    </head>
    <body>
		%for o in objects :
            <% setLang(user.lang) %>
            <div class="contenedor_principal">
                <div class="contenedor_contenido">  
                <div class="act_as_table">
                        <div class="act_as_row">
                            <div class="act_as_cell" style="width:20%;">
                                <div style="position: relative;">
                                    <div style="position: absolute; top: 10px; bottom: 0px;">
                                        ${helper.embed_image('jpeg',str(o.company_emitter_id.logo),130)}                         
                                    </div>                               
                                </div>
                            </div>
                            <div class="act_as_cell" style="width:45%">
                                <div class="act_as_table">
                                    <div class="act_as_row" style="text-align:left; font-weight:bold;">
                                        <div class="act_as_cell" style="padding-top:0px; font-size:15px;">
                                            ${get_emitter_data(o.company_emitter_id.address_invoice_parent_company_id, 'name')}
                                        </div>
                                    </div>
                                    <div class="act_as_row" style="text-align:left;">
                                        <div class="act_as_cell" style="padding-top:0px; padding-bottom:8px;">
                                            ${get_emitter_data(o.company_emitter_id.address_invoice_parent_company_id, 'vat')}
                                        </div>
                                    </div>
                                    <div class="act_as_row" style="text-align:left;">
                                        <div class="act_as_cell" style="padding:0px; font-size:8px;">
                                            ${_("Tax Residence")}
                                        </div>
                                    </div>
                                    <div class="act_as_row" style="text-align:left;">
                                        <div class="act_as_cell" style="padding:0px;">
                                            ${get_emitter_data(o.company_emitter_id.address_invoice_parent_company_id, 'street')} Nro. Ext: ${get_emitter_data(o.company_emitter_id.partner_id, 'no_ext')} Int: ${get_emitter_data(o.company_emitter_id.address_invoice_parent_company_id, 'no_int')} 
                                        </div>
                                    </div>
                                    <div class="act_as_row" style="text-align:left;">
                                        <div class="act_as_cell" style="padding:0px;">
                                            ${_("City")}: 
                                            ${get_emitter_data(o.company_emitter_id.address_invoice_parent_company_id, 'city')} 
                                            ${_("State")}: ${get_emitter_data(o.company_emitter_id.partner_id, 'state')}
                                       </div>
                                    </div>
                                    <div class="act_as_row" style="text-align:left;">
                                        <div class="act_as_cell" style="padding:0px;">
                                            ${_("Location")}: 
                                            ${get_emitter_data(o.company_emitter_id.address_invoice_parent_company_id, 'county') or 'N/A'}
                                       </div>
                                    </div>
                                    <div class="act_as_row" style="text-align:left;">
                                        <div class="act_as_cell" style="padding:0px;">
                                            ${_("ZIP")}: 
                                            ${get_emitter_data(o.company_emitter_id.address_invoice_parent_company_id, 'zip')}
                                       </div>
                                    </div>                    
                                    <div class="act_as_row" style="text-align:left;">
                                        <div class="act_as_cell" style="padding:0px;">
                                            ${_("PHONE")}(s): 
                                            ${o.company_emitter_id.address_invoice_parent_company_id.phone or 'N/A'} 
                                       </div>
                                    </div>
                                </div>
                            </div>
                            <div class="act_as_cell" style="border:1px solid black;">
                                <div class="act_as_table">
                                    <div class="act_as_row">
                                        <div class="act_as_cell" style="color:red; text-align:center; font-size:18px;">
                                            <b>ESTADO DE CUENTA </b>
                                        </div>
                                    </div> 
                                    <div class="act_as_row">
                                        <div class="act_as_cell" style="text-align:center;">                                            
                                            ${time}
                                        </div>
                                    </div> 
                                    <div class="act_as_row">
                                        <div class="act_as_cell" style="text-align:center;">
                                            <b>${o.partner_id.name}</b><br>                                            
                                        </div>
                                    </div> 
                                    <!--
                                    <div class="act_as_row">
                                        <div class="act_as_cell" style="text-align:center;">
                                            <b>DEBE <br>${get_partner_invoice_total(o)[0]} de ${get_partner_invoice_total(o)[1]}</b><br> <br>  
                                        </div>
                                    </div> 
                                    -->                                                                     
                                </div>
                            </div>                             
                        </div>
                    </div>  
                    </br>
                    
                                    
                    <div class="act_as_table">
                        <div class="act_as_row">
                            <div class="act_as_cell" style="border:1px solid #D3D3D3; color:#4B0082; text-align:center; padding:5px;">
                                <b>${_("FACTURA")}</b>
                            </div>
                            <div class="act_as_cell" style="border:1px solid #D3D3D3; color:#4B0082; text-align:center; padding:5px; word-wrap: break-word;">
                                <b>${_("FECHA")}</b>
                            </div>
                            <div class="act_as_cell" style="border:1px solid #D3D3D3; color:#4B0082;text-align:center; padding:5px;">
                                <b>${_("PARCIALIDAD")}</b>
                            </div>
                            <div class="act_as_cell" style="border:1px solid #D3D3D3; color:#4B0082; text-align:center; padding:5px;">
                                <b>${_("ORIGEN")}</b>
                            </div>
                            <!--
                            <div class="act_as_cell" style="border:1px solid #D3D3D3; color:#4B0082; text-align:center; padding:5px;">
                                <b>${_("DEBE")}</b>
                            </div>
                            -->
                            <div class="act_as_cell" style="border:1px solid #D3D3D3; color:#4B0082; text-align:center; padding:5px;">
                                <b>${_("SUBTOTAL")}</b>
                            </div>
                            <div class="act_as_cell" style="border:1px solid #D3D3D3; color:#4B0082; text-align:center; padding:5px;">
                                <b>${_("IVA")}</b>
                            </div>
                            
                            <div class="act_as_cell" style="border:1px solid #D3D3D3; color:#4B0082; text-align:center; padding:5px;">
                                <b>${_("TOTAL")}</b>
                            </div>
                            <div class="act_as_cell" style="border:1px solid #D3D3D3; color:#4B0082; text-align:center; padding:5px;">
                                <b>${_("ESTADO")}</b>
                            </div>
                        </div>
                        %for l in get_invoices(o):
                        <div class="act_as_row">
                            <div class="act_as_cell" style="border:1px solid #D3D3D3; text-align:center; padding:5px;">
                                ${l[1] or 'No identificado'} 
                            </div>
                            <div class="act_as_cell" style="border:1px solid #D3D3D3; text-align:center; padding:5px;">
                                ${l[2] or 'No identificado' }
                            </div>
                            <div class="act_as_cell" style="border:1px solid #D3D3D3; text-align:center; padding:5px;">
                                ${ l[3] or 'No identificado'}
                            </div>
                            <div class="act_as_cell" style="border:1px solid #D3D3D3; text-align:center; padding:5px;">
                                ${ l[4] or 'No identificado'}
                            </div>
                            <!--
                            <div class="act_as_cell" style="border:1px solid #D3D3D3; text-align:center; padding:5px;">
                                ${formatLang(l[5]) or '0.0'}
                            </div>
                            -->
                            <div class="act_as_cell" style="border:1px solid #D3D3D3; text-align:center; padding:5px;">
                                ${formatLang(l[7]) or '0.0'}
                            </div>
                             <div class="act_as_cell" style="border:1px solid #D3D3D3; text-align:center; padding:5px;">
                                ${formatLang(l[6]) or '0.0'}
                            </div>
                            <div class="act_as_cell" style="border:1px solid #D3D3D3; text-align:center; padding:5px;">
                                ${formatLang(l[8]) or '0.0'}
                            </div>
                            <div class="act_as_cell" style="border:1px solid #D3D3D3; text-align:center; padding:5px;">
                               %if l[9] == 'paid': 
                                 	Pagado
                                % else: 
                                	Abierto                                	
                                %endif
                            </div>
                        </div>
                        %endfor
                   </div>   
            </div>
        %endfor
    </body> 
</html>    