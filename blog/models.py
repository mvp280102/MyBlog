from django.db import models
from django.urls import reverse
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=64)
    reg_date = models.DateField(default=timezone.now)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    text = models.TextField()
    pub_date = models.DateField(default=timezone.now)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('blog:index')


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateField(default=timezone.now)
