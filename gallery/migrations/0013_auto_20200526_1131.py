# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-26 08:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0012_auto_20200526_1129'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name_plural': 'location'},
        ),
    ]