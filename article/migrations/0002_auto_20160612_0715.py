# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-12 07:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Articele',
            new_name='Article',
        ),
    ]
