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
from smarturls import surl

lawmaekers_urls = patterns(
    'lawmakers.views',

    surl('/test_crawl_lawmakers/', 'test_crawl_lawmakers', name='test_crawl_lawmakers'),
    
    #for test(amazingguni) 
    surl('/crawl_lawmakers/', 'crawl_lawmakers', name='crawl_lawmakers'),
)

parties_urls = patterns(
    'lawmakers.views',

    surl('/', 'parties', name='parties'),
    surl('/<int:id>/lawmakers/', 'party_lawmakers', name='party_lawmakers'),
    surl('/all/lawmakers/', 'all_party_lawmakers', name='all_party_lawmakers'),
)

articles_urls = patterns(
    'articles.views',

    surl('/', 'articles', name='articles'),
    
    surl('/test_crawl_articles/', 'test_crawl_articles', name='test_crawl_articles'),
)

urlpatterns = [
    surl('admin/', include(admin.site.urls)),

    surl('lawmakers/', include(lawmaekers_urls, namespace='lawmakers')),
    surl('parties/', include(parties_urls, namespace='parties')),
    surl('articles/', include(articles_urls, namespace='articles')),
]
