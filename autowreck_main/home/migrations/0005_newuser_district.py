# Generated by Django 4.1.1 on 2023-01-30 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_car_car_model_alter_car_car_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='district',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
