# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from celery import shared_task
import requests
from bs4 import BeautifulSoup
from lawmakers.models import Lamaker

@shared_task
def crawl_all_articles():
    lawmakers = Lawmaker.objects.all();
    
    for lawmaker in lawmakers:
        _crawl_articles_for(lawmaker.name)

def _crawl_articles_for(name):
    pass