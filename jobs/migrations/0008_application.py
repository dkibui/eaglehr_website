# Generated by Django 4.0.4 on 2022-05-07 18:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_post_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=75)),
                ('last_name', models.CharField(max_length=75)),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.CharField(max_length=17)),
                ('cover_letter', models.FileField(upload_to='uploads/')),
                ('resume', models.FileField(upload_to='uploads/')),
                ('reference', models.CharField(max_length=255)),
                ('date_applied', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
