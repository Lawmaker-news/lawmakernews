# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import
from celery import shared_task
import re
import requests
from bs4 import BeautifulSoup
from lawmakers.models import Lawmaker, Party
import logging
from colorlog import ColoredFormatter


logger = logging.getLogger('lawmakers')

@shared_task
def crawl_all_lawmakers():
    logger.debug('crawl_all_lawmakers start')
    response = requests.get('http://www.rokps.or.kr/profile.asp?code=no19&title=19%B4%EB%C0%C7%BF%F8')
    table = BeautifulSoup(response.text).find(width=550)
    for a_tag in table.find_all('a'):
        _crawl_each_lawmaker('http://www.rokps.or.kr/' + a_tag['href'])

def _crawl_each_lawmaker(url):
    response = requests.get(url)
    table = BeautifulSoup(response.text).find(valign='top', align='left')

    # 이름, 정당, 지역구, 회차 등이 한 문장으로 이어져 있음
    captures = re.search('성 명.{,20}>([가-힣]+).*제(19)대[[가-힣\s]*\((.{,20})\)([가-힣.ㆍ\s]+)', unicode(table), re.DOTALL)

    name = captures.group(1)
    captures2 = re.findall('([가-힣]{2,10})', captures.group(4))
    party = Party.get_party_by_name(re.sub('[^가-힣]', '', captures2[-1]))
    local = re.sub('[^가-힣]', '', captures.group(3))
    generation = captures.group(2)

    logger.debug(name)
    logger.debug(party.name)
    logger.debug(local)
    logger.debug(generation)
    logger.debug('-' * 30)

    Lawmaker(name=name, party=party, local=local, generation=generation, is_current=True).save()
