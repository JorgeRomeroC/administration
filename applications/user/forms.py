from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import User


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ['email', 'password']  # Especifica los campos que quieres en el formulario

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        # Añadir clases de Bootstrap a los campos
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',  # Clases de Bootstrap para estilizar
            'placeholder': 'Email',
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Contraseña',
        })

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            email = self.cleaned_data.get('email')
            if email:
                username = email.split('@')[0]
            else:
                raise forms.ValidationError("El campo email no puede estar vacío cuando se genera un username.")
        return username