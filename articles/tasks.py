# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from celery import shared_task
import time
import re
import requests
from bs4 import BeautifulSoup
from lawmakers.models import Lawmaker
from articles.models import Article

@shared_task
def crawl_all_articles():
    lawmakers = Lawmaker.objects.all();
    
    for lawmaker in lawmakers.iterator():
        _crawl_articles_for(lawmaker)
        time.sleep(2)

def _crawl_articles_for(lawmaker):
    response = requests.get('http://news.naver.com/main/search/search.nhn', params={
            'query': lawmaker.name,
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
        title = title.strip()[1:-1].strip()
        
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

        new_article = Article(title=title, content=content, origin_link=origin_link, thumbnail_link=thumbnail_link, press=press)

        # 국회의원 - 기사 매핑
        _map_articles_lawmakers(new_article, lawmaker)

def _map_articles_lawmakers(article, lawmaker):
    existed_articles = Article.objects.filter(title=article.title)
    
    if existed_articles.exist():
        current_article = existed_articles.first()
    else:
        current_article = article
        current_article.save()

    lawmaker.articles.add(current_article)