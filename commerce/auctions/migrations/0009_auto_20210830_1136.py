# Generated by Django 3.1.5 on 2021-08-30 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_listning_auction_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listning',
            name='image',
            field=models.ImageField(blank=True, default='default.jpeg', null=True, upload_to=''),
        ),
    ]
