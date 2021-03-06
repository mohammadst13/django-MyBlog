from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=100)

    def __str__ (self):
        return self.title

    slug = models.SlugField()

    body = models.TextField()

    def snippet(self):
        return self.body[:50] + " ..."

    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg',blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
