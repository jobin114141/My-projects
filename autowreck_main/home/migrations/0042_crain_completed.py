# Generated by Django 4.1.1 on 2023-04-05 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0041_crain_completed'),
    ]

    operations = [
        migrations.CreateModel(
            name='crain_completed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=25)),
                ('car_number', models.CharField(max_length=25)),
                ('contact_number', models.IntegerField()),
                ('yard_name', models.CharField(max_length=25)),
                ('drop_out_location', models.CharField(max_length=25)),
                ('user_id', models.IntegerField()),
                ('on_going', models.IntegerField(default=0)),
                ('craindriver', models.IntegerField(default=0)),
                ('staring_km', models.IntegerField(default=0)),
                ('end_km', models.IntegerField(default=0)),
                ('total_km', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('completed', models.IntegerField(default=0)),
            ],
        ),
    ]
