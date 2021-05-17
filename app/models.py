# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("O email é obrigatório")
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    # create_user e create_superuser não estão criando certo o usuario para is_staff e is_superuser
    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault(str("is_superuser"), True)
        extra_fields.setdefault(str("is_staff"), True)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault(str("is_superuser"), True)
        extra_fields.setdefault(str("is_staff"), True)

        if extra_fields.get(str("is_superuser")) is not True:
            raise ValueError('Superuser precisa ter is_superuser=true')

        if extra_fields.get(str("is_staff")) is not True:
            raise ValueError('Staff precisa ter is_staff=true')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    name = models.CharField("Nome", max_length=20)
    email = models.EmailField("E-mail", unique=True)
    #password_1 = models.CharField("Senha", max_length=20, default="esoft123456")
    #password_2 = models.CharField("Confirmar senha", max_length=20, default="esoft123456")
    zipcode = models.CharField("CEP", max_length=8, default="12345678")
    address = models.CharField("Endereço", max_length=20, default=" ")
    number = models.CharField("Número", max_length=4, default=" ")
    complement = models.CharField("Complemento", max_length=20, default=" ")
    district = models.CharField("Bairro", max_length=20, default=" ")
    city = models.CharField("Cidade", max_length=20, default=" ")
    state = models.CharField("Estado", max_length=20, default=" ")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'city', 'zipcode', 'address', 'number',
                       'complement', 'district', 'city', 'state']

    def __str__(self):
        return self.email

    objects = UserManager()


class Product(models.Model):
    name = models.CharField("Nome", max_length=15)
    price = models.DecimalField("Preço", decimal_places=2, max_digits=10)
    stock = models.IntegerField("Estoque")

    def __str__(self):
        return self.name
