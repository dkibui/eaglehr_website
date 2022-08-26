from django.contrib import admin
from . import models


@admin.action(description='Activate selected jobs')
def activate_job(modeladmin, request, queryset):
    queryset.update(active=1)


@admin.action(description='Deactivate selected jobs')
def deactivate_job(modeladmin, request, queryset):
    queryset.update(active=0)


class PostAdmin(admin.ModelAdmin):
    def date_posted(self, obj):
        return obj.date_created.date()

    actions = [activate_job, deactivate_job]
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


class JobTypeAdmin(admin.ModelAdmin):
    list_display = ('type_of_job',)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('location',)


# Register your models here.
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Category)
admin.site.register(models.Application, ApplicationAdmin)
admin.site.register(models.Location, LocationAdmin)
admin.site.register(models.JobType, JobTypeAdmin)


# Unregister modules
# admin.site.unregister(Group)
# readonly_fields= ['updated', 'timestamp',]
