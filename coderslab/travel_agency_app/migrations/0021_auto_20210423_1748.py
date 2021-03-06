# Generated by Django 3.2 on 2021-04-23 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel_agency_app', '0020_auto_20210422_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='toCity',
            field=models.CharField(default='Bali', max_length=64),
        ),
        migrations.AlterField(
            model_name='flight',
            name='toCountry',
            field=models.CharField(default='Indonesia', max_length=64),
        ),
        migrations.RemoveField(
            model_name='hotelbooking',
            name='user',
        ),
        migrations.AddField(
            model_name='hotelbooking',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='travel_agency_app.user'),
        ),
        migrations.DeleteModel(
            name='UserHotel',
        ),
    ]
