# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from lawmakernews.settings.base import *

# Debug Mode

DEBUG = True


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lawmakernews_local',
        'USER': 'local_root',
        'PASSWORD': '123123123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Logger

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            '()': 'colorlog.ColoredFormatter',
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S",
            'log_colors': {
                'DEBUG':    'bold_black',
                'INFO':     'white',
                'WARNING':  'yellow',
                'ERROR':    'red',
                'CRITICAL': 'bold_red',
            },
        },
        'simple': {
            'format': '%(levelname)s %(message)s',
        },
    },
    'handlers': {
        'djangofile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'log/django.log',
            'formatter': 'verbose',
        }, 
        'lawmakersfile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'log/lawmakers.log',
            'formatter': 'verbose',
        },
        'articlesfile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'log/articles.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers':['djangofile'],
            'propagate': True,
            'level':'DEBUG',
        },
        'articles': {
            'handlers': ['articlesfile'],
            'level': 'DEBUG',
        }, 
        'lawmakers': {
            'handlers': ['lawmakersfile'],
            'level': 'DEBUG',
        },
    },
}