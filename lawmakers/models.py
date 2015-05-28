# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from articles.models import Article

class Lawmaker(models.Model):
    name = models.CharField(max_length=30)
    party = models.ForeignKey('Party', related_name='lawmakers')
    local = models.CharField(max_length=100)
    generation = models.IntegerField()
    is_current = models.BooleanField()
    articles = models.ManyToManyField(Article, related_name='lawmakers')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Party(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def get_party_by_name(cls, name):
        query_set = cls.objects.filter(name=name)
        if query_set.exists():
            return query_set.first()
        else:
            return cls.objects.filter(name='기타').first()