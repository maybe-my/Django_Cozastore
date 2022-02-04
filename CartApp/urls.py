from django.urls import path
from . import views

app_name = 'CartApp'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<product_id>', views.cart_add, name='cart_add'),
    path('remove/<product_id>', views.cart_remove, name='cart_remove'),
]