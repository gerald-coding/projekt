# Generated by Django 4.1 on 2022-08-12 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_models', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(),
        ),
    ]
