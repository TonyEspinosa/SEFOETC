from django.shortcuts import render

from apps.proveedor.models import m_categoria, m_proveedor #, m_tipo
from django.http import HttpResponse
from .utils import render_to_pdf
from django.contrib.auth.decorators import login_required

import xlwt

# Paginas Privadas
@login_required(login_url='u_usr_login')
def v_inicio(request):
	return render(request,'inicio.html', {})

# Paginas Publicas
def v_home(request):
    qCategoriaTodo = m_categoria.objects.filter(m_proveedor__isnull=False).distinct()
    context =  {'categorias':qCategoriaTodo}
    return render(request, 'public/public_inicio.html', context)

def v_list(request, pk_cat):
    qCatID = m_categoria.objects.get(id_categoria = pk_cat)
    qProvFiltered = qCatID.m_proveedor_set.all()
    #qProvFiltered = m_proveedor.objects.filter(m_categoria__id_categoria=pk_cat)
    context = {'categoria':qCatID, 'proveedor':qProvFiltered}
    return render(request, 'public/public_cat_list.html', context)

# View PDF file
def v_ViewPDF(request, pk_prov):
    qProvID = m_proveedor.objects.get(id_proveedor = pk_prov)
    context = {'proveedor':qProvID}
    pdf = render_to_pdf('public/public_print_pdf.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Proveedor_%s.pdf" %(qProvID.nombre)
        content = "inline; filename=%s" %(filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")

def v_export_excel(request, pk_cat):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=SEFOET.xls'
    
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Categoria')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Nombre', 'Categoria', 'Tipo', 'Descripcion', 'Contacto', 'Puesto', 'Email', 'Tel1', 'Tel2', 'País', 'Estado', 'Ciudad', 'Dirección', 'Sitio Web', 'Facebook', 'Canaco', 'RFC', 'Razón Social']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    
    font_style = xlwt.XFStyle()
    ##font_style.font.bold = False
	
    qCatID = m_categoria.objects.get(id_categoria = pk_cat)
    rows = qCatID.m_proveedor_set.all().values_list('nombre', 'categoria', 'tipo', 'descripcion', 'contacto', 'puesto', 'email', 'tel1', 'tel2', 'pais', 'estado', 'ciudad', 'direccion', 'sitioweb', 'facebook', 'canaco', 'RFC', 'RS')

    for row in rows:
        row_num+=1

        for col_num in range(len(row)):
            if col_num == 1:
                ws.write(row_num, col_num, qCatID.nombre, font_style)
            else:
                ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)

    return response