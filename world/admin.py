from django.contrib import admin
from world.models import Continent, Country
# Register your models here.

@admin.register(Continent)
class ContinentAdmin(admin.ModelAdmin):
    search_fields = ['continent']

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    search_fields = ['country']
    list_display = ('country','get_continent')
    list_filter = ('continent',)

    def get_continent(self, obj):
        return obj.continent.continent
    get_continent.short_description = 'Continente: '
