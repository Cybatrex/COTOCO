# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-09 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20160809_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_code',
            field=models.CharField(default=0, max_length=7, primary_key=True, serialize=False, unique=True, verbose_name='C\xf3digo'),
        ),
    ]