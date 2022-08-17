# Generated by Django 4.0.4 on 2022-08-14 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_models', '0004_rename_car_i_image_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='car_models.car'),
        ),
    ]
