from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import Author, Post
from .utils import authors_context, posts_context


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AuthorsView, self).get_context_data(**kwargs)
        context.update(authors_context)
        return context


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'blog/detail.html'


class PostsView(ListView):
    template_name = 'blog/posts.html'
    context_object_name = 'list'

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostsView, self).get_context_data(**kwargs)
        context.update(posts_context)
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
