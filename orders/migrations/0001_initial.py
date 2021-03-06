# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-25 23:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custumer_name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('custumer_email', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('customer_phone', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('customer_address', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('comments', models.TextField(blank=True, default=None, null=True)),
                ('totalprice', models.DecimalField(decimal_places=5, default=None, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductInOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('number', models.IntegerField(default=1)),
                ('itemprice', models.DecimalField(decimal_places=5, default=None, max_digits=10)),
                ('totalprice', models.DecimalField(decimal_places=5, default=None, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
                ('product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=24, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Status'),
        ),
    ]
