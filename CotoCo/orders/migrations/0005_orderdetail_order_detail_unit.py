# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-12 01:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_orderdetail_order_detail_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='order_detail_unit',
            field=models.CharField(default='', max_length=255, verbose_name='Unidad'),
        ),
    ]