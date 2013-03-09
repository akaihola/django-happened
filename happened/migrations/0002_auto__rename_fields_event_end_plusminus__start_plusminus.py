# -*- coding: utf-8 -*-

from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.rename_column(u'happened_event',
                         'start_plusminus', 'start_resolution')
        db.rename_column(u'happened_event',
                         'end_plusminus', 'end_resolution')

    def backwards(self, orm):
        db.rename_column(u'happened_event',
                         'start_resolution', 'start_plusminus')
        db.rename_column(u'happened_event',
                         'end_resolution', 'end_plusminus')

    models = {
        'happened.event': {
            'Meta': {'object_name': 'Event'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            'end_resolution': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'start_resolution': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        'happened.url': {
            'Meta': {'object_name': 'Url'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['happened.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['happened']
