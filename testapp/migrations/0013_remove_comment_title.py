# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-23 07:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0012_comment_relation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='title',
        ),
    ]
