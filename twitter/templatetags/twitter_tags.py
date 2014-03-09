from django.template import Library
from django.conf import settings as project_settings

from random import random, randrange

import tweepy

from ttp import ttp

import logging

logger = logging.getLogger('django')

register = Library()

consumer_key = getattr(project_settings, "TWITTER_CONSUMER_KEY")
consumer_secret = getattr(project_settings, "TWITTER_CONSUMER_SECRET")

access_token = getattr(project_settings, "TWITTER_ACCESS_KEY")
access_token_secret = getattr(project_settings, "TWITTER_ACCESS_SECRET")

@register.inclusion_tag('tags/twitter/dummy.html')
def twitter_feed(template='tags/twitter/feed.html'):
    """
    Template tag returns a dictionary of twitter objects
    that has had the text parsed and formatted.
    """
    user = "manufacturedba"
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        p = ttp.Parser()
        statuses = []
        for status in tweepy.Cursor(api.user_timeline, id=user).items(5):
            status.text = p.parse(status.text)
            statuses.append(status)
    except tweepy.TweepError:
        pass
        
    return {'template': template,
            'statuses': statuses}
