# Generated by Django 4.1.1 on 2023-01-30 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_newuser_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=55)),
                ('car_model', models.IntegerField()),
                ('yard_name', models.CharField(max_length=255)),
                ('min_amount', models.IntegerField()),
            ],
        ),
    ]
