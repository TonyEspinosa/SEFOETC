from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    #check = forms.BooleanField(required=True)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
        labels = {
            'username': 'Usuario',
            'email': 'Correo Electrónico',
            'password1': 'Contraseña',
            'password2': 'Confirmación',
        }
        widgets = {
            'email':
                forms.EmailInput(attrs={'class':'form-control'}),
            'password1':
                forms.PasswordInput(attrs={'class':'form-control'}),
            'password2':
                forms.PasswordInput(attrs={'class':'form-control'}),
        }