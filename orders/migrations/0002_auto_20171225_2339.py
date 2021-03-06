# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-25 23:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='totalprice',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='itemprice',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='totalprice',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=10),
        ),
    ]
