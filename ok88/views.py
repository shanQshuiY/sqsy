# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import article
import json
# Create your views here.

def index(request):
    all_article = article.objects.all()

    return render(request, 'ok88/index.html', {'all_article':all_article})

def about(request):
    return render(request, 'ok88/about.html')

def detail(request, article_id):
    the_article = article.objects.get(article_id = article_id)
    print the_article.article_content

    spans = json.loads(the_article.article_content)
    out_spans = list()
    for span in spans:
        outspan = {}
        if '{#br#}' in span['content']:
            pass
        else:
            span['content'] = span['content'] + '{#br#}'
        outspan['content1'] = span['content'].split('{#br#}')[0]
        outspan['content2'] = span['content'].split('{#br#}')[1]
        outspan['img'] = span['img']
        #
        # outspan['content'] = span['content'].replace('{#br#}', '</br><img src="{#br#}" alt="Picture" /></br>')
        # outspan['content'] = outspan['content'].replace('{#br#}', span['img'])
        out_spans.append(outspan)
        print out_spans
    return render(request, 'ok88/detail.html', {'article':the_article, 'out_spans':out_spans})