# Generated by Django 4.1.1 on 2023-02-13 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction',
            old_name='price',
            new_name='bid_amount',
        ),
    ]
