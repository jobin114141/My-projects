# Generated by Django 4.1.1 on 2023-04-05 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_alter_crain_craindriver_alter_crain_endinging_km_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crain',
            name='contact_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='crain',
            name='craindriver',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='crain',
            name='endinging_km',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='crain',
            name='staring_km',
            field=models.IntegerField(default=0),
        ),
    ]
