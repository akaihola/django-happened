from django.db import models


class Event(models.Model):
    start = models.DateTimeField()
    start_plusminus = models.IntegerField(default=0)
    end = models.DateTimeField()
    end_plusminus = models.IntegerField(default=0)
    title = models.CharField(max_length=1000)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.title


class Url(models.Model):
    event = models.ForeignKey(Event)
    order = models.IntegerField(default=1)
    url = models.URLField()

    def __unicode__(self):
        return self.url
