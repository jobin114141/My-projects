# Generated by Django 4.1.1 on 2023-04-13 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0047_alter_sold_cars_crain_deliverd'),
    ]

    operations = [
        migrations.AddField(
            model_name='crain',
            name='car_id',
            field=models.IntegerField(default=0),
        ),
    ]
