from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from tweetlocator.views import TweetMapView, TweetUpdateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'maplecroft.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^map-updates',TweetUpdateView.as_view(), name="fetch-tweets"),
    url(r'^', TweetMapView.as_view(), name="map-viewer")

)
