# Generated by Django 4.2 on 2023-04-13 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_products_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip_address',
            field=models.IntegerField(null=True),
        ),
    ]
