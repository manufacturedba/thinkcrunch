from django.template import Library
from django.conf import settings as project_settings

from random import random, randrange

import tweepy

import logging

logger = logging.getLogger('django')

register = Library()

consumer_key = getattr(project_settings, "TWITTER_CONSUMER_KEY")
consumer_secret = getattr(project_settings, "TWITTER_CONSUMER_SECRET")

access_token = getattr(project_settings, "TWITTER_ACCESS_KEY")
access_token_secret = getattr(project_settings, "TWITTER_ACCESS_SECRET")

@register.inclusion_tag('tags/twitter/dummy.html')
def twitter_feed(template='tags/twitter/feed.html'):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    statuses = tweepy.Cursor(api.user_timeline, id="thinkcrunch").items(5)    
    return {'template': template,
            'statuses': statuses}
