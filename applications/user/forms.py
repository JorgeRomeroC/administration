from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import User


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            email = self.cleaned_data.get('email')
            if email:
                username = email.split('@')[0]
            else:
                raise forms.ValidationError("El campo email no puede estar vacío cuando se genera un username.")
        return username
