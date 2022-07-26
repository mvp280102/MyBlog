from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('authors/', views.AuthorsView.as_view(), name='authors'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('posts/', views.PostsView.as_view(), name='posts'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
]
