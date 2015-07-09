from django.db import models
from durationfield.db.models.fields.duration import DurationField
from ckeditor.fields import RichTextField
from django.utils.translation import ugettext as _
from django.db.models import SmallIntegerField

DAY_OF_THE_WEEK = {
    '1': _(u'Monday'),
    '2': _(u'Tuesday'),
    '3': _(u'Wednesday'),
    '4': _(u'Thursday'),
    '5': _(u'Friday'),
    '6': _(u'Saturday'),
    '7': _(u'Sunday'),
}

class DayOfTheWeekField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = tuple(sorted(DAY_OF_THE_WEEK.items()))
        kwargs['max_length'] = 1
        super(DayOfTheWeekField, self).__init__(*args, **kwargs)

class New(models.Model):
    title = models.CharField(max_length=300)
    date = models.DateField()
    time = models.TimeField(blank=True)
    description = models.CharField(max_length=600)
    details = models.TextField()
    picture = models.URLField(blank=True, max_length=500, null=True)
    def picture_url(self):
        return self.picture.url

    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ['-date']

class Broadcast(models.Model):
    title = models.CharField(max_length=300)
    #date = models.DateField()
    time = models.TimeField(blank=True, null=True)
    #description = models.CharField(max_length=600, blank=True)
    #duration = DurationField()
    online = models.BooleanField(default=False)
    day = DayOfTheWeekField(null=True)

    def __unicode__(self):
        return self.title


class Summary(models.Model):
    title = models.CharField(max_length=100)
    online_date = models.DateTimeField(blank=True)
    
    def __unicode__(self):
        return self.title
