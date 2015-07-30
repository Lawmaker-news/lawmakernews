# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""lawmakernews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, patterns, url
from django.contrib import admin

lawmaekers_urls = patterns(
    'lawmakers.views',

    url(r'^$', 'lawmakers', name='lawmakers'),
    url(r'^parties/$', 'parties', name='parties'),
    
    url(r'^test_crawl_lawmakers/$', 'test_crawl_lawmakers', name='test_crawl_lawmakers'),
)

articles_urls = patterns(
    'articles.views',

    url(r'^$', 'articles', name='articles'),
    
    url(r'^test_crawl_articles/$', 'test_crawl_articles', name='test_crawl_articles'),
)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^lawmakers/', include(lawmaekers_urls, namespace='lawmakers')),
    url(r'^articles/', include(articles_urls, namespace='articles')),
    url(r'^$', 'articles.views.index', name='index'),
]