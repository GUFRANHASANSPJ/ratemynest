# Generated by Django 5.0.7 on 2024-11-21 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_property_lat_property_lng'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='bath',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='bed',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
