# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
