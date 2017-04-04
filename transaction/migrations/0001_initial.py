# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 15:46
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date_created', models.DateTimeField(verbose_name='date published')),
                ('date_deleted', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                (
                    'user',
                    models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='creditor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creditor',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transaction',
            name='debtor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debtor',
                                    to=settings.AUTH_USER_MODEL),
        ),
    ]
