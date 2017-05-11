# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 16:07
from __future__ import unicode_literals

import camerabase.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_date', models.DateTimeField(verbose_name='date Event')),
                ('event_pic', models.ImageField(blank=True, null=True, upload_to=camerabase.models.get_image_path)),
            ],
        ),
    ]
