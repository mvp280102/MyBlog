from django.urls import path
from . import views, utils


app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(extra_context=utils.index_context), name='index'),
    path('archive/', views.ArchiveView.as_view(extra_context=utils.archive_context), name='archive'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit', views.PostEditView.as_view(), name='post_edit'),
]
