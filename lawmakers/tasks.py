# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import
from celery import shared_task
import requests
from bs4 import BeautifulSoup

@shared_task
def crawl_all_lawmakers():
    response = requests.get('http://www.rokps.or.kr/profile.asp?code=no19&title=19%B4%EB%C0%C7%BF%F8')
    table = BeautifulSoup(response.text).find(width=550)
    for a_tag in table.find_all('a'):
        crawl_each_lawmaker('http://www.rokps.or.kr/' + a_tag['href'])

def crawl_each_lawmaker(url):
    print url
    print '@@@@@@@@@@@@@@'