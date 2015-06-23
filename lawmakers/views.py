# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict
import json
from lawmakers.models import Lawmaker, Party
from lawmakers.tasks import crawl_all_lawmakers

def lawmakers(request):
    lawmakers = map(lambda lawmaker: model_to_dict(lawmaker, exclude='articles'), Lawmaker.objects.all())
    
    return HttpResponse(json.dumps(lawmakers), content_type='application/json')

def parties(request):
    parties = map(lambda party: model_to_dict(party), Party.objects.all())
    
    return HttpResponse(json.dumps(parties), content_type='application/json')

def test_crawl_lawmakers(request):
    crawl_all_lawmakers.delay()
    
    return render(request, 'temp.html')
