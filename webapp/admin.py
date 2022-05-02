from django.contrib import admin
from django.forms import forms

from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass
