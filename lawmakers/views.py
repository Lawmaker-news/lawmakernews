# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from lamakers.tasks import crawl_all_lamakers

def test_crawl_lawmakers(request):
    crawl_all_lamakers.delay()
    return render('temp.html')
