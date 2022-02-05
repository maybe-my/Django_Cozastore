from django.views.generic import TemplateView, DetailView, ListView
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Index(ListView):
    model = Post
    paginate_by = 2
    template_name = 'BlogApp/blog.html'


class DetailPost(DetailView):
    model = Post
    template_name = 'BlogApp/blog-detail.html'
