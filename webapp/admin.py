from django.contrib import admin
from django.forms import forms

from .models import Event, BannerMessage


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(BannerMessage)
class EventAdmin(admin.ModelAdmin):
    pass
