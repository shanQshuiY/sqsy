# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'ok88/index.html')

def about(request):
    return render(request, 'ok88/about.html')

def detail(request, article_id):
    return render(request, 'ok88/detail.html', {'article_id':article_id})