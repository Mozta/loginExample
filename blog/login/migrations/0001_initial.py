# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-13 23:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.IntegerField()),
                ('nombre', models.CharField(max_length=200)),
                ('ult_periodo', models.CharField(max_length=200)),
                ('tutor', models.CharField(max_length=200)),
                ('avance', models.DecimalField(decimal_places=1, max_digits=3)),
            ],
        ),
    ]
