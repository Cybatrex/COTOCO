# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-12 23:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pays', '0002_auto_20160923_0912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pay',
            name='pay_details',
        ),
        migrations.RemoveField(
            model_name='paydetail',
            name='pay_detail_completed',
        ),
        migrations.AddField(
            model_name='pay',
            name='pay_actual_debt',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True, verbose_name='Saldo Total Actual'),
        ),
        migrations.AddField(
            model_name='pay',
            name='pay_document_num',
            field=models.CharField(default=1, max_length=100, verbose_name='Comprobante N\xfamero'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pay',
            name='pay_last_debt',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True, verbose_name='Saldo Total Anterior'),
        ),
        migrations.AddField(
            model_name='pay',
            name='pay_notes',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Notas'),
        ),
        migrations.AddField(
            model_name='paydetail',
            name='pay_detail_actual_debt',
            field=models.DecimalField(decimal_places=2, max_digits=11, null=True, verbose_name='Saldo Actual'),
        ),
        migrations.AddField(
            model_name='paydetail',
            name='pay_detail_last_debt',
            field=models.DecimalField(decimal_places=2, max_digits=11, null=True, verbose_name='Saldo Anterior'),
        ),
        migrations.AddField(
            model_name='paydetail',
            name='pay_detail_pay',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pays.Pay', verbose_name='Pago'),
            preserve_default=False,
        ),
    ]
