from django.shortcuts import render, HttpResponse
from . import models



def articles_list(request):
    articles = models.Article.objects.all().order_by('date')
    arg = {'articles' : articles}
    return render(request, 'articles/articleslist.html', arg)

def articles_detail(request, slug):
    return HttpResponse(slug)
