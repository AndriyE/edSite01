# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-17 10:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20160105_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('images_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Post')),
            ],
        ),
    ]
