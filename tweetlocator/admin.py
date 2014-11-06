from django.contrib import admin
from models import Tweet, TweetCountry


class TweetCountryAdmin(admin.ModelAdmin):
    list_display = ['name','iso_code','lat','lng','tweet_count']

admin.site.register(Tweet)
admin.site.register(TweetCountry, TweetCountryAdmin)