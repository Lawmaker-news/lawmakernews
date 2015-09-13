# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict
import json
from lawmakers.models import Lawmaker, Party
from lawmakers.tasks import crawl_all_lawmakers, crawl_all_lawmakers_na

def parties(request):
    print 'parties'

    parties = map(lambda party: model_to_dict(party), Party.objects.all())
    
    return HttpResponse(json.dumps(parties), content_type='application/json')

def party_lawmakers(request, id):
    print 'party_lawmakers'

    lawmakers = map(lambda lawmaker: model_to_dict(lawmaker, exclude='articles'), Lawmaker.objects.filter(party=id).all())

    return HttpResponse(json.dumps(lawmakers), content_type='application/json')

def all_party_lawmakers(request, id):
    print 'all_party_lawmakers'
    
    return HttpResponse(json.dumps(lawmakers), content_type='application/json')


def test_crawl_lawmakers(request):
    # crawl_all_lawmakers.delay()
    
    return render(request, 'temp.html')

def crawl_lawmakers(request):
    crawl_all_lawmakers_na.delay()
    
    return render(request, 'temp.html')
