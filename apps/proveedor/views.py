from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

import datetime
import xlwt

from .models import *
from .forms import fm_proveedor

# Create your views here.
@login_required(login_url='u_usr_login')
def v_prov(request):
    qProvTodo = m_proveedor.objects.all()
    context = {'prov':qProvTodo}
    return render(request, 'prov_list.html', context)

@login_required(login_url='u_usr_login')
def v_prov_new(request):
    form = fm_proveedor()
    if request.method == 'POST':
        form = fm_proveedor(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('u_prov_list') 
    context = {'form':form}
    # qProvID = m_proveedor.objects.get(id_proveedor = pk_prov)
    # context = {'prov':qProvID}
    return render(request, 'prov_new.html', context)

@login_required(login_url='u_usr_login')
def v_prov_upd(request, pk_prov):
    qProvID = m_proveedor.objects.get(id_proveedor = pk_prov)
    form = fm_proveedor(instance = qProvID)
    if request.method == 'POST':
        form = fm_proveedor(request.POST, request.FILES, instance = qProvID)
        if form.is_valid():
            form.save()
            return redirect('u_prov_list')
    context = {'form':form}
    return render(request, 'prov_upd.html', context)

@login_required(login_url='u_usr_login')
def v_prov_del(request, pk_prov):
    qProvID = m_proveedor.objects.get(id_proveedor = pk_prov)

    if request.method == "POST":
        qProvID.delete()
        return redirect('u_prov_list')
        
    context = {'item':qProvID}
    return render(request, 'prov_del.html', context)

@login_required(login_url='u_usr_login')
def v_export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Proveedores' + \
        str(datetime.datetime.now()) + '.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Proveedor')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['ID', 'Nombre', 'Categoria', 'Tipo', 'Descripcion', 'Contacto', 'Puesto', 'Telefono 1', 'Telefono 2', 'Pais', 'Estado', 'Ciudad', 'Direccion', 'Sitio WEB', 'Facebook', 'Canaco', 'Razón Social', 'RFC']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    #font_style.font.bold = False

    rows = m_proveedor.objects.all().values_list('id_proveedor', 'nombre', 'categoria', 'tipo', 'descripcion', 'contacto', 'puesto', 'tel1', 'tel2', 'pais', 'estado', 'ciudad', 'direccion', 'sitioweb', 'facebook', 'canaco', 'RS', 'RFC')

    for row in rows:
        row_num+=1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)

    return response