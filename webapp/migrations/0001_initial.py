# Generated by Django 4.0.4 on 2022-04-28 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('start_date', models.DateField(auto_now=True)),
                ('duration', models.DurationField()),
                ('cost', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
