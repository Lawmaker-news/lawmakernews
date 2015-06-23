# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict
import json
from articles.models import Article
from articles.tasks import crawl_all_articles

def articles(request):
    articles = map(lambda article: model_to_dict(article, exclude='lawmakers'), Article.objects.all())

    return HttpResponse(json.dumps(articles), content_type='application/json')

def test_crawl_articles(request):
    crawl_all_articles.delay()

    return render(request, 'temp.html')
