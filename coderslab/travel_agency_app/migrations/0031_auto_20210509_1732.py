# Generated by Django 3.2 on 2021-05-09 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_agency_app', '0030_auto_20210509_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=5),
        ),
        migrations.DeleteModel(
            name='MyRating',
        ),
    ]
