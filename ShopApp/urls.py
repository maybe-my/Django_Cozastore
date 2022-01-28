from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('detail/<slug>', views.DetailProduct.as_view(), name='detail_product'),
    path('add_email/', views.Newsletter, name='Newsletter')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
