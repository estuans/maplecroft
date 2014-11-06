from datetime import datetime

from django.db import models

class Tweet(models.Model):
    """
    This model is used for caching tweets rather than spamming the Twitter API and getting rate limited.
    """
    author = models.CharField(max_length=64)
    tweet = models.TextField()

    created = models.DateTimeField(default=datetime.now,blank=True,null=True)
    tweet_created = models.DateTimeField(blank=True,null=True)
    tweet_id = models.CharField(max_length=32,null=True,blank=True)

    country_of_interest = models.ManyToManyField('TweetCountry',blank=True, null=True)

    def __unicode__(self):
        return "%s : %s" % (";".join(i.name for i in self.country_of_interest.all()), self.tweet_created)

    def save(self,*args,**kwargs):
        if not self.created:
            self.created = datetime.now()

        super(Tweet,self).save(*args,**kwargs)

    def guess_countries(self):
        country_list = TweetCountry.objects.all()
        for i in country_list:
            if i.name in self.tweet:
                i.tweet_set.add(self)
                i.save()

class TweetCountry(models.Model):

    class Meta:
        verbose_name_plural = "Tweet Countries"

    name = models.CharField(max_length=128)
    iso_code = models.CharField(max_length=2)
    lat = models.CharField(max_length=16,blank=True,null=True)
    lng = models.CharField(max_length=16,blank=True,null=True)

    def tweet_count(self):
        return self.tweet_set.all().count()

    def __unicode__(self):
        return self.name