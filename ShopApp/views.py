from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Product


class Index(TemplateView):
    template_name = 'ShopApp/index.html'


class DetailProduct(DetailView):
    model = Product
    # slug_field = 'product'
    template_name = 'ShopApp/product-detail.html'
