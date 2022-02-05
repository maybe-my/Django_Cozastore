from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('search/', views.SearchProduct.as_view(), name='search_product'),
    path('order/', include('OrdersApp.urls')),
    path('products/', views.ProductList.as_view(), name='products_list'),
    path('detail/<slug>', views.DetailProduct.as_view(), name='detail_product'),
    path('about/', views.About.as_view(), name='about'),
    path('contact/', views.Contact.as_view(), name='contact'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)