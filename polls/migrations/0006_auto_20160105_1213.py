# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-05 11:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_post_posts_auftor_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comments_post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.Post'),
            preserve_default=False,
        ),
    ]
