#!/usr/bin/python
# -*- coding: <utf-8> -*-

from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200, verbose_name='Название статьи')
    image = models.CharField(max_length=255, verbose_name='Ссылка на картинку')
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    image = models.CharField(max_length=255, verbose_name='Ссылка на картинку')
    alias = models.SlugField(verbose_name='Alias категории')

class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название товара')
    price = models.IntegerField(default=0, verbose_name='Цена')
    image = models.CharField(max_length=255, verbose_name='Ссылка на картинку')
    alias = models.SlugField(verbose_name='Alias товара')
    published_date = models.DateTimeField(
            blank=True, null=True)

    category = models.ForeignKey(Category)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
