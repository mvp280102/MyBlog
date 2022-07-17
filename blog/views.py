from django.shortcuts import render
from .models import Post


def index(request):
    post_list = Post.objects.order_by('-pub_date')
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)
