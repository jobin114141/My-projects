# Generated by Django 4.1.1 on 2023-04-13 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0044_crain_craindriver_name_crain_craindriver_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crain',
            name='car_number',
            field=models.CharField(default=False, max_length=25),
        ),
    ]
