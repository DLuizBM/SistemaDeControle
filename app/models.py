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
    zipcode = models.CharField("CEP", max_length=8, default="Ex: 72800000")
    address = models.CharField("Endereço", max_length=20, default="Ex: Rua 21 de Abril")
    number = models.CharField("Número", max_length=4, default="Ex: 25")
    complement = models.CharField("Complemento", max_length=20, default="Ex: Setor sul")
    district = models.CharField("Bairro", max_length=20, default="Ex: Ipanema")
    city = models.CharField("Cidade", max_length=20, default="Ex: Rio de Janeiro")
    state = models.CharField("Estado", max_length=20, default="Ex: RJ")

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    objects = UserManager()


class Product(models.Model):
    name = models.CharField("Nome", max_length=15)
    price = models.DecimalField("Preço", decimal_places=2, max_digits=10)
    stock = models.IntegerField("Estoque")

    def __str__(self):
        return self.name
