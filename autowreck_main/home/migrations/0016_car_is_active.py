# Generated by Django 4.1.1 on 2023-02-08 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_car_image2_car_image3_car_image4_car_image5'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='is_active',
            field=models.BooleanField(default=0),
        ),
    ]
