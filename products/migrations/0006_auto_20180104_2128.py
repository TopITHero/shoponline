# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-04 21:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20171226_0045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='categoty',
            new_name='category',
        ),
    ]