# Generated by Django 4.1.1 on 2023-02-03 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_car_img1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='battery',
            field=models.IntegerField(),
        ),
    ]
