# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=50)),
                ('house', models.CharField(max_length=5)),
                ('room', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Tarif',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tarif_name', models.CharField(max_length=30)),
                ('abonplata', models.PositiveIntegerField()),
                ('services', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contract', models.PositiveIntegerField()),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40)),
                ('phone_num', models.CharField(max_length=15, blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('abon_tarif', models.ManyToManyField(to='users.Tarif')),
            ],
        ),
    ]
