# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Continent(models.Model):
    continent = models.CharField(max_length=20)

    def __unicode__(self):
        return self.continent

    class Meta:
        verbose_name = 'Continente'

class Country(models.Model):
    country = models.CharField(max_length=40, verbose_name=u'País')
    capital = models.CharField(max_length=40, verbose_name='Capital')
    coin = models.CharField(max_length=30, verbose_name='Moeda')
    language = models.CharField(max_length=20, verbose_name='Idioma')
    continent = models.ForeignKey(Continent,verbose_name='Continente')

    def __unicode__(self):
        return self.country

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Paises'
