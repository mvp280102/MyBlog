from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import Author, Post


class IndexView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'lists'

    def get_queryset(self):
        return Author.objects.order_by('-reg_date')[:5], Post.objects.order_by('-pub_date')[:5]


class AuthorsView(ListView):
    template_name = 'blog/authors.html'
    context_object_name = 'list'

    def get_queryset(self):
        return Author.objects.order_by('-reg_date')


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'blog/detail.html'


class PostsView(ListView):
    template_name = 'blog/posts.html'
    context_object_name = 'list'

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
