# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-07 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcari', '0047_comment_se'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='se',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
