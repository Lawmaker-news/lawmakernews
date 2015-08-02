# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from lawmakernews.settings.base import *

# Debug Mode

DEBUG = True


# Template setting for local enviroments

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'client/src/html'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'client/src'),)

STATIC_URL = '/client/'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('LOCAL_DB_NAME'),
        'USER': os.environ.get('LOCAL_DB_USER'),
        'PASSWORD': os.environ.get('LOCAL_DB_PASSWORD'),
        'HOST': os.environ.get('LOCAL_DB_HOST'),
        'PORT': os.environ.get('LOCAL_DB_PORT'),
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