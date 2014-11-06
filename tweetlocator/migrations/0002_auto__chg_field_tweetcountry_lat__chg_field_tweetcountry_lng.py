# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'TweetCountry.lat'
        db.alter_column(u'tweetlocator_tweetcountry', 'lat', self.gf('django.db.models.fields.CharField')(max_length=16, null=True))

        # Changing field 'TweetCountry.lng'
        db.alter_column(u'tweetlocator_tweetcountry', 'lng', self.gf('django.db.models.fields.CharField')(max_length=16, null=True))

    def backwards(self, orm):

        # Changing field 'TweetCountry.lat'
        db.alter_column(u'tweetlocator_tweetcountry', 'lat', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'TweetCountry.lng'
        db.alter_column(u'tweetlocator_tweetcountry', 'lng', self.gf('django.db.models.fields.FloatField')(null=True))

    models = {
        u'tweetlocator.tweet': {
            'Meta': {'object_name': 'Tweet'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'country_of_interest': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tweetlocator.TweetCountry']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tweet': ('django.db.models.fields.TextField', [], {})
        },
        u'tweetlocator.tweetcountry': {
            'Meta': {'object_name': 'TweetCountry'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso_code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'lng': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['tweetlocator']