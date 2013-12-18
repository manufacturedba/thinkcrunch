# Django Development Settings for Local

from thinkcrunch.settings.base import *

DEBUG = True
STATIC_DEBUG = False

TEMPLATE_DEBUG = DEBUG

SITE_ID = 1

DEFAULT_FROM_EMAIL = 'messenger@localhost'
SERVER_EMAIL = DEFAULT_FROM_EMAIL

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'thinkcrunch',                       # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'manufacturedba',
        'PASSWORD': 'ed15633335',
        'HOST': '',                       # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                       # Set to empty string for default.
    }
}


TIME_ZONE = 'US/Eastern'

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = ('127.0.0.1', )

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Overwrite default ROOT_URLCONF to include static file serving by Django.
# In production, this should be handled separately by your webserver or CDN.
ROOT_URLCONF = 'thinkcrunch.urls.dev'

COMPRESS_OFFLINE = False
COMPRESS_ENABLED = False

EMAIL_PORT = 1025

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

COMPRESS_CACHE_BACKEND = "default"

if not STATIC_DEBUG:
    STATIC_URL = 'http://static.thinkcrunch.com.s3.amazonaws.com/'
    MEDIA_URL = '/media/'
    ROOT_URLCONF = 'thinkcrunch.urls.production'

    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    STATICFILES_STORAGE = DEFAULT_FILE_STORAGE

    COMPRESS_URL = STATIC_URL
    COMPRESS_STORAGE = DEFAULT_FILE_STORAGE
    COMPRESS_OFFLINE = False

    AWS_ACCESS_KEY_ID = 'AKIAJ7WR3NUFVC6R2AXQ'

    AWS_SECRET_ACCESS_KEY = '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'

    AWS_STORAGE_BUCKET_NAME = 'static.thinkcrunch.com'

    AWS_HEADERS = {
		    'x-amz-acl': 'public-read',
		    'Cache-Control': 'no-cache, max-age=%d' % max_age,
		    }
		
    AWS_S3_SECURE_URLS = False
