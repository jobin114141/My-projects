# Generated by Django 4.1.1 on 2023-04-05 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_crain_endinging_km_crain_staring_km'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crain',
            name='craindriver',
            field=models.IntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='crain',
            name='endinging_km',
            field=models.IntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='crain',
            name='staring_km',
            field=models.IntegerField(default=True),
        ),
    ]
