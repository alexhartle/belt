# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolCreator', '0002_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='name',
            field=models.TextField(default='MysteryUser', max_length=255),
            preserve_default=False,
        ),
    ]
