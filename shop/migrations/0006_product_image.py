# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-20 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_remove_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, upload_to='Products'),
        ),
    ]
