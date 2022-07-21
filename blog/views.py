from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import Post


class IndexView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')[:5]


class ArchiveView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')


class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/create.html'
    fields = ['author', 'title', 'text']


class PostEditView(UpdateView):
    model = Post
    template_name = 'blog/edit.html'
    fields = ['title', 'text']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
