# Generated by Django 4.1.1 on 2023-02-14 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auction_largest_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='largest_bid',
            field=models.IntegerField(default=False),
        ),
    ]
