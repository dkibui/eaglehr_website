from django.contrib import admin
from django.forms import forms

from .models import Event, BannerMessage


@admin.action(description='Activate selected events')
def activate_event(modeladmin, request, queryset):
    queryset.update(is_active=1)


@admin.action(description='Deactivate selected events')
def deactivate_event(modeladmin, request, queryset):
    queryset.update(is_active=0)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    actions = [activate_event, deactivate_event]
    list_display = ['name', 'is_active', 'start_date', 'duration']
    ordering = ['start_date']


@admin.action(description='Deactivate selected banner messages')
def deactivate_banner_message(modeladmin, request, queryset):
    queryset.update(is_active=0)


@admin.register(BannerMessage)
class EventAdmin(admin.ModelAdmin):
    actions = [deactivate_banner_message]
    list_display = ['name', 'is_active']
