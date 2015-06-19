# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from articles.tasks import crawl_all_articles, _crawl_articles_for

def test_crawl_articles(request):
    crawl_all_articles.delay()
    # _crawl_articles_for.delay(name='haha')
    return render(request, 'temp.html')
