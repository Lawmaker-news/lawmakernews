# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=1024)
    content = models.CharField(max_length=1024)
    origin_created_at = models.DateTimeField()
    origin_link = models.URLField(max_length=2048)
    thumnail_link = models.URLField(max_length=2048)
    press_company = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)