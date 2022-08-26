from django.contrib import admin
from . import models


@admin.action(description='Activate selected blogs')
def activate_blogs(modeladmin, request, queryset):
    queryset.update(active=1)


@admin.action(description='Deactivate selected blogs')
def deactivate_blogs(modeladmin, request, queryset):
    queryset.update(active=0)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name', ]


class BlogsAdmin(admin.ModelAdmin):
    def date_posted(self, obj):
        return obj.date_created.date()

    actions = [activate_blogs, deactivate_blogs]
    list_display = ('title', 'date_posted', 'active')
    search_fields = ['title', 'content']
    list_filter = ("active",)
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(models.Blogs, BlogsAdmin)
admin.site.register(models.Category, CategoryAdmin)
