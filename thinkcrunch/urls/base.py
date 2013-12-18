from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.defaults import *
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from cms.sitemaps import CMSSitemap

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^xmlrpc/$', 'django_xmlrpc.views.handle_xmlrpc'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^weblog/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^', include('cms.urls')),
)
