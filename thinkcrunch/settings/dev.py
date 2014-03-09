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
    PROJECT_ROOT = os.path.join(ROOT_PATH, 'static/')
    COMPRESS_ROOT = STATIC_ROOT
    
    STATIC_URL = "http://static.thinkcrunch.com/"
    MEDIA_URL = STATIC_URL + 'media/'
    COMPRESS_URL = STATIC_URL
    ROOT_URLCONF = 'thinkcrunch.urls.production'

    DEFAULT_FILE_STORAGE = 'thinkcrunch.storage.CachedS3BotoStorage'
    STATICFILES_STORAGE = DEFAULT_FILE_STORAGE
    COMPRESS_STORAGE = DEFAULT_FILE_STORAGE
    
    
    COMPRESS_ENABLED = False
    COMPRESS_OFFLINE = False
    
    AWS_S3_SECURE_URLS = False
    AWS_ACCESS_KEY_ID = 'AKIAJ7WR3NUFVC6R2AXQ'

    AWS_SECRET_ACCESS_KEY = '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'

    AWS_STORAGE_BUCKET_NAME = 'static.thinkcrunch.com'
    import boto.s3.connection
#    AWS_S3_CALLING_FORMAT = boto.s3.connection.VHostCallingFormat()

#    AWS_QUERYSTRING_AUTH = False
    AWS_HEADERS = {
		    'x-amz-acl': 'public-read',
            'Cache-Control': 'public, max-age=31556926'
		    }
	
