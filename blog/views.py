from django.views.generic import ListView, DetailView
from .models import Author, Post
from .utils import index_context, authors_context, posts_context


class IndexView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'lists'

    def get_queryset(self):
        return Author.objects.order_by('-reg_date')[:5], Post.objects.order_by('-pub_date')[:5]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(index_context)
        return context


class AuthorsView(ListView):
    context_object_name = 'list'

    def get_queryset(self):
        return Author.objects.order_by('-reg_date')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AuthorsView, self).get_context_data(**kwargs)
        context.update(authors_context)
        return context


class AuthorDetailView(DetailView):
    model = Author
    context_object_name = 'author'


class PostsView(ListView):
    context_object_name = 'list'

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostsView, self).get_context_data(**kwargs)
        context.update(posts_context)
        return context


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
