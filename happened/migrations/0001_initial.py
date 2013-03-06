# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table(u'happened_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start', self.gf('django.db.models.fields.DateTimeField')()),
            ('start_plusminus', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('end', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_plusminus', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'happened', ['Event'])

        # Adding model 'Url'
        db.create_table(u'happened_url', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['happened.Event'])),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'happened', ['Url'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table(u'happened_event')

        # Deleting model 'Url'
        db.delete_table(u'happened_url')


    models = {
        u'happened.event': {
            'Meta': {'object_name': 'Event'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            'end_plusminus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'start_plusminus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        u'happened.url': {
            'Meta': {'object_name': 'Url'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['happened.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['happened']