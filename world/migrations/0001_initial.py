# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('continent', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Continente',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(max_length=40, verbose_name='Pa\xeds')),
                ('capital', models.CharField(max_length=40, verbose_name=b'Capital')),
                ('coin', models.CharField(max_length=30, verbose_name=b'Moeda')),
                ('language', models.CharField(max_length=20, verbose_name=b'Idioma')),
                ('continent', models.ForeignKey(verbose_name=b'Continente', to='world.Continent')),
            ],
            options={
                'verbose_name': 'Pa\xeds',
                'verbose_name_plural': 'Paises',
            },
        ),
    ]
