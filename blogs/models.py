from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'


class ActiveBlogManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=1)


class Blogs(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = RichTextField()
    slug = models.SlugField(max_length=255, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, default=0,
                               on_delete=models.CASCADE)
    active = models.BooleanField(
        default=False, help_text='Select to publish this blog article. De-select to hide this blog article from displayed articles.')

    objects = models.Manager()
    active_blog = ActiveBlogManager()

    class Meta:
        ordering = ['-date_created', 'author']
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.title
