from django.contrib import admin
from . import models


@admin.action(description="Activate selected news")
def activate_news(modeladmin, request, queryset):
    queryset.update(active=1)


@admin.action(description="Deactivate selected news")
def deactivate_news(modeladmin, request, queryset):
    queryset.update(active=0)


class NewsAdmin(admin.ModelAdmin):
    def date_posted(self, obj):
        return obj.date_created.date()

    actions = [activate_news, deactivate_news]
    list_display = ("title", "date_posted", "active")
    search_fields = ["title", "content"]
    list_filter = ("active",)
    prepopulated_fields = {"slug": ("title",)}


# Register your models here.
admin.site.register(models.News, NewsAdmin)
