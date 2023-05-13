from django.db import models

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
class m_categoria(models.Model):
    id_categoria = models.AutoField(primary_key = True, db_column='id_categoria')

    nombre = UpperCharField(max_length=250, null=True, verbose_name = "Nombre", uppercase=True)
    color = models.CharField(max_length=7, null=True, verbose_name = "Color")
    descripcion = models.TextField(max_length=500, null=True, verbose_name = "Descripción")
    image = models.ImageField(upload_to="categoria", null=True, verbose_name="Foto", blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, verbose_name = "Creación")

    class Meta:
        db_table = 'categoria'
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["nombre"]

    def __str__(self) -> str:
        return self.nombre  # type: ignoree

    def setColorCategory():
        COLORS = {
            1 : '#FFCC00', #Amarillo
            2 : '#76B82A', #Verde
            3 : '#50BCBD', #Aguamarina
            4 : '#0D9982', #Esmeralda
            5 : '#0C6250', #Verde obscuro
            6 : '#F07D17', #Naranja
            7 : '#EB5E5E', #Rosado
            8 : '#00A8E4', #Azul cielo
            9 : '#0062AE', #Azul
            10 : '#242F62', #Azul Rey
        }

        qCat = m_categoria.objects.all()
        if qCat:
            cont = 0
            for a in qCat:
                a.color = COLORS[(cont % 10)+1]
                a.save()
                cont+=1