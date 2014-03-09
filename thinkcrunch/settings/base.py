# Common settings and globals.

# -*- coding: utf-8 -*-
import os, sys
import thinkcrunch as project_module

from zinnia.xmlrpc import ZINNIA_XMLRPC_METHODS

gettext = lambda s: s
max_age = 31556926

PROJECT_ROOT = os.path.dirname(os.path.realpath(project_module.__file__))
ROOT_PATH = os.path.dirname(__file__)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
 ('Roberto Rodriguez', 'roberto@thinkcrunch.com'),
)

MANAGERS = ADMINS

SITE_ID = 1

TIME_ZONE = 'US/Eastern'

LANGUAGE_CODE = 'en-us'

USE_I18N = False

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

MEDIA_URL = STATIC_URL + 'media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'assets'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

SECRET_KEY = '5c8wut3bys&amp;c&amp;ppx8)f)w48#p(kngbm_8f84d_z9aygp))k0r)'


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
    'thinkcrunch.context_processors.site',
)
    
MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'thinkcrunch.urls'

WSGI_APPLICATION = 'thinkcrunch.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.comments',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangocms_text_ckeditor',
    'cms',
    'cms.stacks',
    'mptt',
    'tagging',
    'menus',
    'south',
    'reversion',
    'sekizai',
    'filer',
    'easy_thumbnails',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',
    'crispy_forms',
    'twitter',
    'cmsplugin_contact',
    'zinnia',
    'cmsplugin_zinnia',
    'registration',
    'registration_bootstrap',
    'django_bitly',
    'storages',
    'compressor',
    'django_xmlrpc',
)

ACCOUNT_ACTIVATION_DAYS = 7

CMS_PERMISSION = True

LANGUAGES = [
    ('en', 'English'),
]

CMS_TEMPLATES = (
('index.html', gettext('Main Page')),
('page.html', gettext('Secondary Page')),
)

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

TEXT_SAVE_IMAGE_FUNCTION='cmsplugin_filer_image.integrations.ckeditor.create_image_plugin'


SERVER_EMAIL = 'roberto@thinkcrunch.com'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'roberto@thinkcrunch.com'
EMAIL_HOST_PASSWORD = 'ed1563335'
EMAIL_PORT = 587

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': { 
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
        'simple': {
            'format': '%(levelname)s %(message)s'
            }
        },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
            },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
            },
            
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}

CACHE_MIDDLEWARE_SECONDS = max_age

COMPRESS_PARSER = 'compressor.parser.BeautifulSoupParser'
COMPRESS_STORAGE = 'compressor.storage.GzipCompressorFileStorage'
COMPRESS_ENABLED = True
	
"""COMPRESS_OFFLINE_CONTEXT = {
    'path_to_files': '/static/js/',
}"""

BITLY_LOGIN = 'manufacturedba'
BITLY_API_KEY = 'R_8beee1fcfd128afe431e54decfd54c19'

#ZINNIA_ENTRY_BASE_MODEL = 'cmsplugin_zinnia.placeholder.EntryPlaceholder'
ZINNIA_URL_SHORTENER_BACKEND = 'zinnia.url_shortener.backends.bitly'
ZINNIA_SPAM_CHECKER_BACKENDS = ('zinnia.spam_checker.backends.long_enough',)

TWITTER_CONSUMER_KEY = 'YI6OgLQczqENjGfKH2Hw'
TWITTER_CONSUMER_SECRET = '9CRUexrzQQ9GIGA0Dw7S0lEYMxg5I2DCLPNleSPkA'
TWITTER_ACCESS_KEY = '574173383-rnBTpWhh1638w6JbF3v6ePXNAihldwUhnJt6hFMw'
TWITTER_ACCESS_SECRET = 'XDf3fZAdMMGcFnCD4biHqZURt8fueZ23b7gJAiakc'

XMLRPC_METHODS = ZINNIA_XMLRPC_METHODS
