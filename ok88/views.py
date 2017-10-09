# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import article
# Create your views here.

def index(request):
    all_article = article.objects.all()

    return render(request, 'ok88/index.html', {'all_article':all_article})

def about(request):
    return render(request, 'ok88/about.html')

def detail(request, article_id):
    the_article = article.objects.get(article_id = article_id)
    return render(request, 'ok88/detail.html', {'article':the_article})