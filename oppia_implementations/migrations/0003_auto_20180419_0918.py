# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-19 09:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oppia_implementations', '0002_auto_20180108_1130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oppiaimplementation',
            old_name='organsiation_url',
            new_name='organisation_url',
        ),
    ]
