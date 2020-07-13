from django.shortcuts import render, HttpResponse
from . import models



def articles_list(request):
    articles = models.Article.objects.all().order_by('-date')
    arg = {'articles' : articles}
    return render(request, 'articles/articleslist.html', arg)

def articles_detail(request, slug):
    # return HttpResponse(slug)
    article = models.Article.objects.get(slug=slug)
    arg = {'article' : article}
    return render(request, 'articles/articles_detail.html', arg)
