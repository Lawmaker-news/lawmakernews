# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from celery import shared_task
import re
import requests
from bs4 import BeautifulSoup
from lawmakers.models import Lawmaker

@shared_task
def crawl_all_articles():
    lawmakers = Lawmaker.objects.all();
    
    for lawmaker in lawmakers:
        _crawl_articles_for(lawmaker.name)

@shared_task
def _crawl_articles_for(name):
    response = requests.get('http://news.naver.com/main/search/search.nhn', params={
            'query': '심상정',
            'ie': 'utf-8',
        })
    articles = BeautifulSoup(response.text).find(id='search_div').find_all('ul', recursive=False)

    for article in articles:
        ct_div = article.find('div', class_='ct')

        info_div = ct_div.find('div', class_='info')
        date = info_div.find('span', class_='time').stripped_string
        if re.match('[0-9]*일전', unicode(date)):
            continue
        press = info_div.find('span', class_='press').string
        
        title_a = ct_div.find('a', class_='tit')
        title = ''
        for string in title_a.stripped_strings:
            title += ' ' + string
        origin_link = title_a['href']
        
        content_p = ct_div.find('p', class_='dsc')
        content = ''
        for string in content_p.stripped_strings:
            content += ' ' + string

        thumbnail_a = article.find('a', class_='thmb')
        thumbnail_link = ''
        if thumbnail_a:
            thumbnail_link = thumbnail_a.find('img')['src']

        print(title)
        print(content)
        print(origin_link)
        print(thumbnail_link)
        print(press)
        print('-' * 30)