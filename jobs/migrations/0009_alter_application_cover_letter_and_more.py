# Generated by Django 4.0.4 on 2022-05-08 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='cover_letter',
            field=models.FileField(upload_to='applications/uploads/'),
        ),
        migrations.AlterField(
            model_name='application',
            name='resume',
            field=models.FileField(upload_to='applications/uploads/'),
        ),
    ]