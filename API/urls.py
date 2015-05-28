# -*- coding: utf-8 -
from api import ContinentResource, CountryResource
from django.conf.urls import patterns, include, url
from tastypie.api import Api


api_urls = Api(api_name='api')
api_urls.register(ContinentResource())
api_urls.register(CountryResource())

urlpatterns = patterns('',
    url(r'', include(api_urls.urls)),
)
