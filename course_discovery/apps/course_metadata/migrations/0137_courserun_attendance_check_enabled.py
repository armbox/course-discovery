# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2020-03-05 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0136_program_course_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='courserun',
            name='attendance_check_enabled',
            field=models.BooleanField(default=False),
        ),
    ]
