# -*- coding: utf-8 -*-
from tastypie.resources import ModelResource
from world.models import Continent, Country

class ContinentResource(ModelResource):
    class Meta:
        queryset = Continent.objects.all()
        resource_name = 'continent'

class CountryResource(ModelResource):
    class Meta:
        queryset = Country.objects.all()
        resource_name = 'country'
