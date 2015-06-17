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
    
    # 검색결과의 1페이지만 가져온다
    articles = BeautifulSoup(response.text).find(id='search_div').find_all('ul', recursive=False)

    for article in articles:
        ct_div = article.find('div', class_='ct')

        info_div = ct_div.find('div', class_='info')
        
        # 최근 24시간 안의 기사만 가져온다
        date = info_div.find('span', class_='time').string
        is_after_day = re.match('.*[0-9]*일전.*', unicode(date))
        is_after_week = re.match('.*[0-9]{4}.[0-9]{2}.[0-9]{2}.*', unicode(date))
        if is_after_day or is_after_week:
            continue
        
        # 언론사
        press = info_div.find('span', class_='press').string
        
        title_a = ct_div.find('a', class_='tit')

        # 원본 링크
        origin_link = title_a['href']
        
        # 제목
        title = ''
        for string in title_a.stripped_strings:
            title += ' ' + string
        
        content_p = ct_div.find('p', class_='dsc')

        # 간추린 내용
        content = ''
        for string in content_p.stripped_strings:
            content += ' ' + string

        thumbnail_a = article.find('a', class_='thmb')

        # 썸네일 이미지 링크
        thumbnail_link = ''
        if thumbnail_a:
            thumbnail_link = thumbnail_a.find('img')['src']

        print(title)
        print(content)
        print(origin_link)
        print(thumbnail_link)
        print(press)
        print('-' * 30)