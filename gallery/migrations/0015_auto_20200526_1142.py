# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-26 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0014_auto_20200526_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='locs',
            field=models.CharField(choices=[('Kenya', 'Kenya'), ('Uganda', 'Uganda'), ('Paris', 'Paris'), ('London', 'London'), ('Mexico', 'Mexico'), ('India', 'India')], max_length=255),
        ),
    ]
