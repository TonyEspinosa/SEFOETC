from django.shortcuts import render, redirect
from django.http import HttpResponse

import datetime
import xlwt

from django.contrib import messages
from .querys import qUsrTodo
from django.contrib.auth.models import User

#Login
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#Captcha
from django.conf import settings
import urllib
import json

@login_required(login_url='u_usr_login')
def v_usr(request):
   context = {'usrs':qUsrTodo}
   return render(request, 'usr_list.html', context)

@login_required(login_url='u_usr_login')
def v_usr_new(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Se creo la cuenta de usuario para ' + user)
            return redirect('u_usr_list')

    context = {'form':form}
    return render(request, 'usr_new.html', context)

@login_required(login_url='u_usr_login')
def v_usr_upd(request, pk_usr):
    qUsrID = User.objects.get(username = pk_usr)
    form = CreateUserForm(instance = qUsrID)
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Se creo la cuenta de usuario para ' + user)
            return redirect('u_usr_list')

    context = {'form':form}
    return render(request, 'usr_upd.html', context)

@login_required(login_url='u_usr_login')
def v_usr_del(request, pk_usr):
   qUsrID = User.objects.get(username = pk_usr)

   if request.method == "POST":
       qUsrID.delete()
       return redirect('u_usr_list')
        
   context = {'item':qUsrID}
   return render(request, 'usr_del.html', context)

## Login
def v_usr_login(request):
    if request.user.is_authenticated:
        return redirect('u_home_priv')
    else:
        if request.method == 'POST':
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''

            if result['success']:
                uname = request.POST.get('username')
                pword = request.POST.get('password')

                user = authenticate(request, username=uname, password=pword)
                if user is not None:
                    login(request, user)
                    return redirect('u_home_priv')
                else:
                    messages.info(request, 'Usuario o contraseña incorrectos...')
            else:
                messages.error(request, 'reCAPTCHA invalido. Intenta nuevamente...')
        context = {}
        return render(request, 'usr_login.html', context)

## Logout
@login_required(login_url='u_usr_login')
def v_usr_logout(request):
    logout(request)
    return redirect('u_usr_login')

## Change Password
@login_required(login_url='u_usr_login')
def v_usr_chng(request):
    pass

@login_required(login_url='u_usr_login')
def v_export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Usuario' + \
        str(datetime.datetime.now()) + '.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Usuario')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Nombre']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    #font_style.font.bold = False

    #rows = m_categoria.objects.all().values_list('nombre', 'descripcion')

    for row in qUsrTodo:
        print(row)
        row_num+=1

        ws.write(row_num, col_num, str(row), font_style)

    wb.save(response)

    return response