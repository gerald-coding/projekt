# Generated by Django 4.0.4 on 2022-08-17 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_models', '0006_alter_booking_pickup_date_alter_booking_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]