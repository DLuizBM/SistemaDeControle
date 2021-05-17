# -*- coding: utf-8 -*-
import json
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Product
from .forms import CustomUserCreationForm, ProductForm
from django.contrib import messages


def product_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products.html', context)


def create_product_view(request):
    form = ProductForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto salvo com sucesso!')
            return redirect('products')
        else:
            messages.error(request, 'Erro ao cadastrar produto.')


def update_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto atualizado com sucesso!')
            return redirect('products')
        else:
            messages.error(request, 'Erro ao atualizar produto.')


def delete_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product:
        product.delete()
        return redirect('products')


def register_view(request):
    form = CustomUserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            form = CustomUserCreationForm()
            return redirect('index')
        else:
            messages.error(request, 'Erro ao cadastrar usuário.')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def home_view(request):
    return render(request, 'home.html')


def data_product_view(request):
    queryset = Product.objects.all()
    product_name = [product.name for product in queryset]
    product_stock = [product.stock for product in queryset]

    context = {
        'names': product_name,
        'stock': product_stock
    }
    return HttpResponse(json.dumps(context))


def order_product_name_view(request):
    queryset = Product.objects.order_by('name')
    context = {
        'products': queryset
    }
    print context
    return render(request, 'products.html', context)


def order_product_price_view(request):
    queryset = Product.objects.order_by('price').reverse()
    context = {
        'products': queryset
    }
    print context
    return render(request, 'products.html', context)


def order_product_stock_view(request):
    queryset = Product.objects.order_by('stock').reverse()
    context = {
        'products': queryset
    }
    print context
    return render(request, 'products.html', context)
