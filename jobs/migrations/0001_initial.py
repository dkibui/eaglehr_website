# Generated by Django 4.0.4 on 2022-06-08 09:05

import ckeditor.fields
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
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=55)),
                ('phone', models.CharField(max_length=13)),
                ('cover_letter', models.FileField(upload_to='applications/uploads/')),
                ('resume', models.FileField(upload_to='applications/uploads/')),
                ('reference', models.CharField(choices=[('website', 'Our own website'), ('employee', 'Eaglehr Employee'), ('social', 'Social Media'), ('internet', 'Internet Search'), ('friend', 'Friend'), ('newspaper', 'Newspaper')], default='website', max_length=255)),
                ('date_applied', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_job', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Job types',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('apply_by_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=False, help_text='Select to publish this job on the job portal page. De-select to hide this job.')),
                ('author', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.category')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.location')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.jobtype')),
            ],
            options={
                'ordering': ['-date_created', 'author'],
            },
        ),
    ]
