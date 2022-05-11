# Generated by Django 4.0.4 on 2022-05-07 17:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='resume',
            field=models.FileField(default=django.utils.timezone.now, upload_to='uploads'),
            preserve_default=False,
        ),
    ]