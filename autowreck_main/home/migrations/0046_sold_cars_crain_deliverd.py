# Generated by Django 4.1.1 on 2023-04-13 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0045_alter_crain_car_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='sold_cars',
            name='crain_deliverd',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
