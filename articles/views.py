# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from articles.tasks import crawl_all_articles, _crawl_articles_for
from articles.models import Article

def articles(request):
    articles = map(lambda article: model_to_dict(article, exclude='lawmakers'), Article.objects.all())

    return HttpResponse(json.dumps(articles), content_type='application/json')

def test_crawl_articles(request):
    crawl_all_articles.delay()
    # _crawl_articles_for.delay(name='haha')
    return render(request, 'temp.html')
