#forms.py
import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class RegistrationForm(forms.Form):

    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Usuario"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("contrasena"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("contrasena (otra vez)"))

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("El usuario ya existe. Por favor intenta con otro."))

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("Las contrasenas no coinciden."))
        return self.cleaned_data

class ListaF(forms.Form):
    matricula = forms.IntegerField()
    nombre = forms.CharField(max_length=200)
    ult_periodo = forms.CharField(max_length=200)
    tutor = forms.CharField(max_length=200)
    avance = forms.DecimalField(max_digits=3, decimal_places=1)

class ModifyF(forms.Form):
    matricula = forms.IntegerField()
    nombre = forms.CharField(max_length=200)
    ult_periodo = forms.CharField(max_length=200)
    tutor = forms.CharField(max_length=200)
    avance = forms.DecimalField(max_digits=3, decimal_places=1)
