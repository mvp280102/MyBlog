from django.shortcuts import get_object_or_404, render
from .models import Post


def index(request):
    post_list = Post.objects.order_by('-pub_date')
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})
