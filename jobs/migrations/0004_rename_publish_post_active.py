# Generated by Django 4.0.4 on 2022-05-03 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_rename_is_published_post_publish_alter_post_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publish',
            new_name='active',
        ),
    ]