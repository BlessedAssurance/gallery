# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-24 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_auto_20200524_2333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cate', models.CharField(choices=[('Flowers', 'Flowers'), ('Articles', 'Articles'), ('Animals', 'Animals'), ('People', 'People')], max_length=255)),
            ],
        ),
    ]
