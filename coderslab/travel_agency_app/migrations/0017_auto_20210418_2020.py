# Generated by Django 3.2 on 2021-04-18 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_agency_app', '0016_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(default='Rome', max_length=64),
        ),
        migrations.AlterField(
            model_name='location',
            name='continent',
            field=models.CharField(default='Europe', max_length=64),
        ),
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.CharField(default='Italy', max_length=64),
        ),
    ]
