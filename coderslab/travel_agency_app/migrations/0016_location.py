# Generated by Django 3.2 on 2021-04-18 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_agency_app', '0015_flight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('continent', models.CharField(max_length=64)),
                ('country', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=64)),
            ],
        ),
    ]
