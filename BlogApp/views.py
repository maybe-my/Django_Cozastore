from django.views.generic import TemplateView, DetailView, ListView
from .models import Post
from ShopApp.models import Product


class Index(ListView):
    model = Post
    paginate_by = 2
    template_name = 'BlogApp/blog.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['last_product'] = Product.objects.all().order_by('-created')[:3]
        return context


class DetailPost(DetailView):
    model = Post
    template_name = 'BlogApp/blog-detail.html'
