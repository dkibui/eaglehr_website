# Generated by Django 4.0.4 on 2022-05-02 21:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='uploads/')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_published', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=0)),
                ('author', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_created', 'author'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_published', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=0)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.post')),
            ],
        ),
    ]