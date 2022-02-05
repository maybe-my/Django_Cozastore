from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = 'BlogApp'

urlpatterns = [
    path('', views.Index.as_view(), name='blog_index'),
    path('detail/<slug>', views.DetailPost.as_view(), name='blog_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)