from django.contrib import admin
from django.contrib.auth.models import Group
import datetime
from . import models


class PostAdmin(admin.ModelAdmin):
    def date_posted(self, obj):
        return obj.date_created.date()

    list_display = ('title', 'date_posted', 'active')
    search_fields = ['title', 'content']
    list_filter = ("active", "author")
    prepopulated_fields = {'slug': ('title',)}


class ApplicationAdmin(admin.ModelAdmin):
    def fullname(self):
        return f'{self.first_name} {self.last_name}'
    list_display = (fullname, 'cover_letter', 'resume')

    readonly_fields = ['first_name', 'last_name', 'cover_letter', 'resume',
                       'email', 'phone', 'reference', 'date_applied', ]


# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Application, ApplicationAdmin)
admin.site.register(models.Post, PostAdmin)


# Unregister modules
# admin.site.unregister(Group)
# readonly_fields= ['updated', 'timestamp',]
