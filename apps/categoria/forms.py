from django.forms import ModelForm
from .models import m_categoria

class fm_categoria(ModelForm):
    class Meta:
        model = m_categoria
        #fields = '__all__'
        fields = ['nombre', 'descripcion', 'image']