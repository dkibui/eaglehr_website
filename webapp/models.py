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
    publish = models.IntegerField(choices=STATUS, default=0)

    def __str__(self) -> str:
        return self.name
