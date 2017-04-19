# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thai_name', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('class_name', models.CharField(max_length=200)),
                ('order', models.CharField(max_length=200)),
                ('family', models.CharField(max_length=200)),
            ],
        ),
    ]
