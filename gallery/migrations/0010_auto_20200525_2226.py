# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-25 19:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0009_auto_20200524_2336'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='images',
            options={},
        ),
        migrations.AddField(
            model_name='images',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='images',
            name='image_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.Category'),
        ),
        migrations.AddField(
            model_name='images',
            name='image_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.Location'),
        ),
        migrations.AlterField(
            model_name='images',
            name='description',
            field=models.TextField(),
        ),
    ]