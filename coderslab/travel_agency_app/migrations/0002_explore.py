# Generated by Django 2.2.17 on 2021-04-17 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_agency_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Explore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('explore', models.CharField(max_length=64)),
            ],
        ),
    ]
