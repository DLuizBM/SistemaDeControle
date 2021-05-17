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
        # username', 'password1', 'password2', são atributos do CustomUser
        fields = ('name', 'username', 'password1', 'password2',
                  'zipcode', 'address', 'number', 'complement',
                  'district', 'city', 'state')
        labels = {'username': 'Username/Email', 'password1': 'Senha', 'password2': 'Confirmar senha'}
        UserCreationForm.error_messages = {'password_mismatch': 'As senhas não combinam'}
        widgets = {
            'zipcode': forms.TextInput(attrs={"id": "id_zipcode", "onblur": "getAddressFields()"}),
        }
        Field.default_error_messages = {'required': ""}
        # com widgets é possível alterarmos e inserir coisas dentro do formulário html do django

    def clean(self):
        """
        name = self.cleaned_data['name']
        #email = self.cleaned_data['email']
        email = self.cleaned_data['username']
        # por que 'username' e não 'email'? self.cleaned_data traz o conteúdo do form enviado
        # se eu fizer um form manual, posso definir o id e o name da tag html com 'username'para
        # o campo email, não precisa estar amarrado ao nome da variável, mas sim, ao colocado no html
        password_1 = self.cleaned_data['password1']
        #password_2 = self.cleaned_data['password2']
        zipcode = self.cleaned_data['zipcode']
        address = self.cleaned_data['address']
        print self.cleaned_data

        """
        try:
            name = self.cleaned_data['name']
        except KeyError:
            raise ValidationError(_("O nome não pode ser vazio."))

        try:
            email = self.cleaned_data['username']
        except KeyError:
            raise ValidationError(_("O Username/Email não pode ser vazio."))

        try:
            number = self.cleaned_data['number']
        except KeyError:
            raise ValidationError(_("O número deve ter pelo menos 1 caractere."))

        try:
            zipcode = self.cleaned_data['zipcode']
        except KeyError:
            raise ValidationError(_("O CEP não pode ser vazio."))

        try:
            address = self.cleaned_data['address']
        except KeyError:
            raise ValidationError(_("O endereço não pode ser vazio."))

        try:
            complement = self.cleaned_data['complement']
        except KeyError:
            raise ValidationError(_("O complemento não pode ser vazio."))

        try:
            district = self.cleaned_data['district']
        except KeyError:
            raise ValidationError(_("O bairro não pode ser vazio."))

        try:
            city = self.cleaned_data['city']
        except KeyError:
            raise ValidationError(_("A cidade não pode ser vazia."))

        try:
            state = self.cleaned_data['state']
        except KeyError:
            raise ValidationError(_("O estado não pode ser vazio."))

        return self.cleaned_data

    # def get_password_1(self):
    #   return self.cleaned_data['password_1']

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        # if self.get_password_1():
        #   self.cleaned_data["password1"] = self.get_password_1()
        ''''
        original = self.cleaned_data["password1"]
        print original
        self.cleaned_data["password1"] = "divino123456789"
        print self.cleaned_data["password1"]
        self.cleaned_data["password1"] = original'''
        user.set_password(self.cleaned_data["password1"])
        # self.cleaned_data['username'] = self.get_email()
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
