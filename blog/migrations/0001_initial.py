# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Название категории', max_length=255)),
                ('image', models.CharField(verbose_name='Ссылка на картинку', max_length=255)),
                ('alias', models.SlugField(verbose_name='Alias категории')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Название товара', max_length=255)),
                ('price', models.IntegerField(verbose_name='Цена', default=0)),
                ('image', models.CharField(verbose_name='Ссылка на картинку', max_length=255)),
                ('alias', models.SlugField(verbose_name='Alias товара')),
                ('published_date', models.DateTimeField(null=True, blank=True)),
                ('category', models.ForeignKey(to='blog.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Название статьи', max_length=200)),
                ('image', models.CharField(verbose_name='Ссылка на картинку', max_length=255)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
