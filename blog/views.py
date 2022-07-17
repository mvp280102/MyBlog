from django.views.generic import ListView, DetailView
from .models import Post


class IndexView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
