# Django Staging Settings for Heroku

import os

from thinkcrunch.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SITE_ID = 1

DEFAULT_FROM_EMAIL = 'roberto@thinkcrunch.com'
SERVER_EMAIL = DEFAULT_FROM_EMAIL

import dj_database_url
DATABASES = {'default' : dj_database_url.config()}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

TIME_ZONE = 'US/Eastern'


INTERNAL_IPS = ('127.0.0.1', )

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

ROOT_URLCONF = 'thinkcrunch.urls.staging'

def get_cache():
	try:
		os.environ['MEMCACHE_SERVERS'] = os.environ['MEMCACHIER_SERVERS' , '']
		os.environ['MEMCACHE_USERNAME'] = os.environ['MEMCACHIER_USERNAME', '']
		os.environ['MEMCACHE_PASSWORD'] = os.environ['MEMCACHIER_PASSWORD', '']
		return {
			'default': {
			'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
			'LOCATION': os.environ['MEMACHIER_SERVERS', ''],
			'TIMEOUT': 500,
			'BINARY': True
				}
			}
	except:
		return {
			'default': {
				'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
				}
			}

CACHES = get_cache()
COMPRESS_CACHE_BACKEND = 'default'
