# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Product
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django import forms
from django.forms import Field


class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Confirmar senha'
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

    class Meta:
        model = CustomUser
        fields = ('name', 'username', 'password1', 'password2',
                  'zipcode', 'address', 'number', 'complement',
                  'district', 'city', 'state')
        labels = {'username': 'Login', 'password1': 'Senha', 'password2': 'Confirmar senha'}
        UserCreationForm.error_messages = {'password_mismatch': 'As senhas não combinam'}
        widgets = {
            'zipcode': forms.TextInput(attrs={"id": "id_zipcode", "onblur": "getAddressFields()"}),
        }
        Field.default_error_messages = {'required': ""}

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data['username']
        user.is_staff = True
        user.is_superuser = True
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('name', 'city')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'stock')

    def clean(self):
        price = self.cleaned_data['price']
        stock = self.cleaned_data['stock']

        if price < 0:
            raise ValueError(_("O preço do produto não pode ser menor do que zero."))

        if stock < 0:
            raise ValueError(_("A quantidade em estoque não pode ser menor que zero."))
