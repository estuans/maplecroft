
import tweepy

from django.conf import settings

from .models import Tweet


class TwitterManager(object):
    api = None
    def __init__(self):
        self.auth()

    def auth(self):
        auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
        auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth)

    def fetch_tweets(self):

        statuses = self.api.user_timeline(settings.SCREEN_NAME, count=20)
        self.store_tweets(statuses)

    def fetch_latest_tweets(self):
        newest_local_tweet = Tweet.objects.all().reverse().first()
        if newest_local_tweet:
            latest_tweets = self.api.user_timeline(settings.SCREEN_NAME, count=20, since_id=newest_local_tweet.tweet_id)
            self.store_tweets(latest_tweets)
            return latest_tweets
        else:
            self.fetch_tweets()
            return self.fetch_latest_tweets()

    def store_tweets(self,statuses):
        for tweet in statuses:
            tweet, created = Tweet.objects.get_or_create(tweet=tweet.text,tweet_created=tweet.created_at,tweet_id=tweet.id)
            if created:
                tweet.guess_countries()
                tweet.save()