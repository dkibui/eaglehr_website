# Generated by Django 4.0.4 on 2022-06-22 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='post',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='jobs.post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='cover_letter',
            field=models.FileField(upload_to='uploads/applications/'),
        ),
        migrations.AlterField(
            model_name='application',
            name='resume',
            field=models.FileField(upload_to='uploads/applications/<django.db.models.fields.related.ForeignKey>'),
        ),
    ]
