# Generated by Django 3.2 on 2021-04-18 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_agency_app', '0009_alter_hotelbooking_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userhotel',
            name='date',
        ),
    ]
