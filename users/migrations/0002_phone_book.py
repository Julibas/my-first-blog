# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone_book',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('f_name', models.CharField(max_length=20)),
                ('s_name', models.CharField(max_length=30, blank=True)),
                ('phone', models.CharField(max_length=40)),
            ],
        ),
    ]
