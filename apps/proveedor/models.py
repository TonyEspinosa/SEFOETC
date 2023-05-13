from django.db import models
#from django.contrib.auth.models import User
from apps.categoria.models import m_categoria

class UpperCharField(models.CharField):
    def __init__(self, *args, **kwargs):
        self.is_uppercase = kwargs.pop('uppercase', False)
        super(UpperCharField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        value = super(UpperCharField, self).get_prep_value(value)
        if self.is_uppercase:
            return value.upper()

        return value

    def from_db_value(self, value, expression, connection, context=None):
        if self.is_uppercase:
            return value.upper()

        return value

# Create your models here.
class m_tipo(models.Model):
    id_tipo = models.AutoField(primary_key = True, db_column='id_tipo')
    
    nombre = UpperCharField(max_length=150, null=True, verbose_name = "Nombre", uppercase=True)
    image = models.ImageField(upload_to="tipo", null=True, verbose_name="Foto", blank=True)

    date_created = models.DateTimeField(auto_now_add=True, null=True, verbose_name = "Creación")

    class Meta:
        db_table = 'tipo'
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"
        ordering = ["nombre"]

    def __str__(self) -> str:
        return self.nombre

class m_proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key = True, db_column='id_proveedor')
    
    nombre = models.CharField(max_length=150, null=True, verbose_name = "Nombre")
    categoria = models.ForeignKey(m_categoria, null=True, verbose_name = "Categoria", on_delete=models.SET_NULL)
    tipo = models.ForeignKey(m_tipo, null=True, verbose_name = "Tipo", on_delete=models.SET_NULL)
    descripcion = models.TextField(max_length=500, null=True, blank=True, verbose_name = "Descripción")
    contacto = models.CharField(max_length=150, null=True, verbose_name = "Contacto")
    puesto = models.CharField(max_length=150, null=True, blank=True, verbose_name = "Puesto")
    email = models.EmailField(max_length=150, null=True, verbose_name = "Email")
    tel1 = models.CharField(max_length=150, null=True, verbose_name = "Teléfono 1")
    tel2 = models.CharField(max_length=150, null=True, blank=True, verbose_name = "Teléfono 2")
    pais = models.CharField(max_length=250, null=True, blank=True, verbose_name = "País")
    estado = models.CharField(max_length=150, null=True, blank=True, verbose_name = "Estado")
    ciudad = models.CharField(max_length=150, null=True, blank=True, verbose_name = "Ciudad")
    direccion = models.CharField(max_length=250, null=True, blank=True, verbose_name = "Dirección")
    sitioweb = models.URLField(max_length=250, null=True, blank=True, verbose_name = "Sitio Web")
    facebook = models.CharField(max_length=250, null=True, blank=True, verbose_name = "Facebook")
    presentacion = models.FileField(upload_to="document", max_length=250, null=True, blank=True, verbose_name = "Presentación")
    canaco = models.BooleanField(default=True, verbose_name = "Canaco")
    RS = models.CharField(max_length=250, null=True, blank=True, verbose_name = "Razón Social")
    RFC = models.CharField(max_length=15, null=True, blank=True, verbose_name = "RFC")
    
    #usuario = models.ForeignKey(User, null=True, verbose_name = "Usuario", on_delete=models.SET_NULL)

    date_created = models.DateTimeField(auto_now_add=True, null=True, verbose_name = "Creación")

    class Meta:
        db_table = 'proveedor'
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ["nombre"]

    def __str__(self) -> str:
        return '%s %s' % (self.nombre, self.tipo)