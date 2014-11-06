# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Tweet.country_of_interest'
        db.delete_column(u'tweetlocator_tweet', 'country_of_interest_id')

        # Adding field 'Tweet.tweet_created'
        db.add_column(u'tweetlocator_tweet', 'tweet_created',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding M2M table for field country_of_interest on 'Tweet'
        m2m_table_name = db.shorten_name(u'tweetlocator_tweet_country_of_interest')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tweet', models.ForeignKey(orm[u'tweetlocator.tweet'], null=False)),
            ('tweetcountry', models.ForeignKey(orm[u'tweetlocator.tweetcountry'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tweet_id', 'tweetcountry_id'])


    def backwards(self, orm):
        # Adding field 'Tweet.country_of_interest'
        db.add_column(u'tweetlocator_tweet', 'country_of_interest',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tweetlocator.TweetCountry'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Tweet.tweet_created'
        db.delete_column(u'tweetlocator_tweet', 'tweet_created')

        # Removing M2M table for field country_of_interest on 'Tweet'
        db.delete_table(db.shorten_name(u'tweetlocator_tweet_country_of_interest'))


    models = {
        u'tweetlocator.tweet': {
            'Meta': {'object_name': 'Tweet'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'country_of_interest': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tweetlocator.TweetCountry']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tweet': ('django.db.models.fields.TextField', [], {}),
            'tweet_created': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
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