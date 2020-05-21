# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-09-24 05:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0134_auto_20190904_0505'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='logo_image_url',
            field=models.URLField(blank=True, help_text='Logo used for program', null=True),
        ),
    ]