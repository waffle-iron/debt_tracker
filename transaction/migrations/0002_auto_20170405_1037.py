# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 08:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='description',
            field=models.TextField(),
        ),
    ]
