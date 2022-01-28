from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import TemplateView, DetailView, ListView
from .models import Product, News


class Index(ListView):
    model = Product
    template_name = 'ShopApp/index.html'


class DetailProduct(DetailView):
    model = Product
    template_name = 'ShopApp/product-detail.html'


def Newsletter(request):
    if request.method == 'POST':
        p = News(email=request.POST['email'])
        p.save()
        return redirect('index')