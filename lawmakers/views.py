# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from lawmakers.tasks import crawl_all_lawmakers

def test_crawl_lawmakers(request):
    crawl_all_lawmakers.delay()
    return render(request, 'temp.html')
