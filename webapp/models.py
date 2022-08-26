from datetime import date, datetime, timedelta
from django.db import models
from ckeditor.fields import RichTextField

# 2022-07-11 # .filter(start_date__gt=current_time)


class ActiveEventManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=1)


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField()
    start_date = models.DateField()
    duration = models.IntegerField(
        default=1, help_text='Duration of course in days')
    cost = models.FloatField(default=10000, blank=True, null=True)
    location = models.CharField(max_length=255)
    is_active = models.BooleanField(
        default=False, help_text='Activate to display this event on homepage on the upcoming events section. Only 3 '
                                 'nearest are displayed.')

    objects = models.Manager()  # The default manager.
    active_event = ActiveEventManager()  # Our custom manager.

    def __str__(self) -> str:
        return self.name


class BannerMessage(models.Model):
    name = models.CharField(max_length=255)
    message = RichTextField()
    is_active = models.BooleanField(
        default=False, help_text='Activate to display this message at the top of the home page')

    def __str__(self) -> str:
        return self.name
