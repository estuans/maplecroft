from __future__ import absolute_import

import json
from maplecroft.celery import app

from .models import Tweet
from .utils import TwitterManager

@app.task
def fetch_latest_tweets():
    tweets = TwitterManager().fetch_latest_tweets()
    db_tweets = []

    for i in tweets:
        tweet = Tweet.objects.get(tweet_id=i.id)
        if tweet:
            db_tweets.append(tweet)

    jtweets = [{"tweet": tweet.tweet,
                "tweet_id": tweet.tweet_id,
                "tweet_created": tweet.tweet_created.isoformat(),
                "countries": [{ "name" : country.name,
                                "lat" : country.lat,
                                "lng" : country.lng,
                                "tweets" : country.tweet_count()
                              } for country in tweet.country_of_interest.all()]
               } for tweet in db_tweets]

    return jtweets