from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, DetailView, ListView
from .models import Product, News
from CartApp.cart import Cart
from CartApp.forms import CartAddProductForm


def get_cart(requests):
    cart = Cart(requests)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return cart


class Index(ListView):
    model = Product
    template_name = 'ShopApp/index.html'
    queryset = Product.objects.all()[:16]

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['cart'] = get_cart(self.request)
        return context


class DetailProduct(DetailView):
    model = Product
    template_name = 'ShopApp/product-detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailProduct, self).get_context_data(**kwargs)
        context['cart'] = get_cart(self.request)
        context['form'] = CartAddProductForm
        return context


class ProductList(ListView):
    model = Product
    queryset = Product.objects.all()[:16]
    template_name = 'ShopApp/product.html'

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context['cart'] = get_cart(self.request)

        return context


class About(ListView):
    model = Product
    template_name = 'ShopApp/about.html'

    def get_context_data(self, **kwargs):
        context = super(About, self).get_context_data(**kwargs)
        context['cart'] = get_cart(self.request)

        return context


class Contact(ListView):
    model = Product
    template_name = 'ShopApp/contact.html'

    def get_context_data(self, **kwargs):
        context = super(Contact, self).get_context_data(**kwargs)
        context['cart'] = get_cart(self.request)

        return context