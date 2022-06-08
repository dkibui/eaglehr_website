from django.db import models

from ckeditor.fields import RichTextField


class Event(models.Model):
    STATUS = (
        (0, "No"),
        (1, "Yes")
    )
    name = models.CharField(max_length=255)
    description = RichTextField()
    start_date = models.DateField()
    duration = models.IntegerField(
        default=1, help_text='Duration of course in days')
    cost = models.FloatField(default=10000, blank=True, null=True)
    location = models.CharField(max_length=255)
    is_active = models.BooleanField(
        default=False, help_text='Activate to display this event on homepage on the upcoming events section. Only 3 nearest are displayed.')

    def __str__(self) -> str:
        return self.name


class BannerMessage(models.Model):
    name = models.CharField(max_length=255)
    message = RichTextField()
    is_active = models.BooleanField(
        default=False, help_text='Activate to display this message at the top of the home page')

    def __str__(self) -> str:
        return self.name
