from django.contrib import admin

# Register your models here.
from .models import m_tipo, m_proveedor

admin.site.register(m_tipo)
admin.site.register(m_proveedor)

