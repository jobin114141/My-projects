# Generated by Django 4.1.1 on 2023-04-05 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_alter_crain_contact_number_alter_crain_craindriver_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crain',
            name='on_going',
            field=models.IntegerField(default=0),
        ),
    ]
