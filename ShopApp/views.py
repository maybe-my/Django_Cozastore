from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, DetailView, ListView
from .models import Product, News
from CartApp.cart import Cart
from CartApp.forms import CartAddProductForm


def Index(request):
    cart = Cart(request)
    form = CartAddProductForm
    tovars_all = Product.objects.all()[:16]
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    return render(request, 'ShopApp/index.html', {'cart': cart, 'form': form, 'product_list': tovars_all})


class DetailProduct(DetailView):
    model = Product
    template_name = 'ShopApp/product-detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailProduct, self).get_context_data(**kwargs)
        context['form'] = CartAddProductForm

        return context


def Newsletter(request):
    if request.method == 'POST':
        p = News(email=request.POST['email'])
        p.save()
        return redirect('index')