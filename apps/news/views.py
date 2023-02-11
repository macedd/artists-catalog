from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from django.views import generic

from .models import Article


# receives slug and redirect to actual article link
def detail_redirect(request, article_slug):
    try:
        article = Article.objects.get(slug=article_slug)
    except Artist.DoesNotExist:
        raise Http404("Article does not exist")
    article.views_increment()
    return redirect(article.link)


# receives id and redirect to current slug
def detail_canonical(request, artist_id):
    try:
        article = Article.objects.get(id=artist_id)
    except Artist.DoesNotExist:
        raise Http404("Article does not exist")
            
    return redirect('news:detail', article_slug=article.slug, permanent=False)
