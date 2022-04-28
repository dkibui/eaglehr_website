from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    duration = models.IntegerField(default=1, help_text='Number of Days')
    cost = models.FloatField(default=10000, blank=True, null=True)

    def __str__(self) -> str:
        return self.name
