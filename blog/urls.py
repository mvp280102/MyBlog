from django.urls import path
from . import views, utils


app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(extra_context=utils.index_context), name='index'),
    path('authors/', views.AuthorsView.as_view(extra_context=utils.authors_context), name='authors'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('posts/', views.PostsView.as_view(extra_context=utils.posts_context), name='posts'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
]
