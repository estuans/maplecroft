# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tweet'
        db.create_table(u'tweetlocator_tweet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('tweet', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('country_of_interest', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tweetlocator.TweetCountry'], null=True, blank=True)),
        ))
        db.send_create_signal(u'tweetlocator', ['Tweet'])

        # Adding model 'TweetCountry'
        db.create_table(u'tweetlocator_tweetcountry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('iso_code', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('lat', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('lng', self.gf('django.db.models.fields.FloatField')(null=True)),
        ))
        db.send_create_signal(u'tweetlocator', ['TweetCountry'])


    def backwards(self, orm):
        # Deleting model 'Tweet'
        db.delete_table(u'tweetlocator_tweet')

        # Deleting model 'TweetCountry'
        db.delete_table(u'tweetlocator_tweetcountry')


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
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'lng': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['tweetlocator']