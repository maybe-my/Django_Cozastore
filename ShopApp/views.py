from django.views.generic import DetailView, ListView
from .models import Product
from CartApp.cart import Cart
from CartApp.forms import CartAddProductForm
from django.db.models import Q


def get_cart(requests):
    cart = Cart(requests)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return cart


class Index(ListView):
    model = Product
    template_name = 'ShopApp/index.html'
    queryset = Product.objects.filter(available=True)[:16]


class DetailProduct(DetailView):
    model = Product
    template_name = 'ShopApp/product-detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailProduct, self).get_context_data(**kwargs)
        context['form'] = CartAddProductForm
        return context


class ProductList(ListView):
    model = Product
    queryset = Product.objects.filter(available=True)[:16]
    template_name = 'ShopApp/product.html'


class SearchProduct(ListView):
    model = Product
    template_name = 'ShopApp/product.html'

    def get_queryset(self):
        return Product.objects.filter(
            Q(name__icontains=self.request.GET['search'], available=True) |
            Q(category__name__icontains=self.request.GET['search'], available=True)
        )


class About(ListView):
    model = Product
    template_name = 'ShopApp/about.html'


class Contact(ListView):
    model = Product
    template_name = 'ShopApp/contact.html'
