# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 00:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0009_auto_20170503_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='animalimage',
            name='status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Published', 'Published')], max_length=10, null=True),
        ),
    ]