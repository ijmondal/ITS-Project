# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-30 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20170830_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Dob', models.DateField()),
                ('Gender', models.CharField(max_length=2)),
            ],
        ),
    ]
