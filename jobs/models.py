from django.db import models
from django.forms import CharField
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
# from taggit.managers import TaggableManager

from ckeditor.fields import RichTextField
from .reference_choices import default_option, WAYS_TO_FIND_US


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


# Create your models here.
STATUS = (
    (0, "No"),
    (1, "Yes")
)


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = RichTextField()
    slug = models.SlugField(max_length=255, unique=True)
    date_created = models.DateTimeField(default=timezone.now)
    apply_by_date = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, default=0,
                               on_delete=models.CASCADE)
    active = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-date_created', 'author']

    def __str__(self):
        return self.title


class Application(models.Model):

    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    email = models.EmailField(max_length=75)
    phone = models.CharField(max_length=13, )
    cover_letter = models.FileField(
        upload_to='applications/uploads/')
    resume = models.FileField(upload_to='applications/uploads/')
    reference = models.CharField(
        max_length=255,
        choices=WAYS_TO_FIND_US,
        default=default_option)
    date_applied = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
