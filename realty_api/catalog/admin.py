from django.contrib import admin
from .models import RealEstate, Location, PropertyType
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

class LocationInline(NestedStackedInline):
    model = Location
    extra = 1
    fk_name = 'real_estate'


class RealEstateAdmin(NestedModelAdmin):
    model = RealEstate
    inlines = [LocationInline]


admin.site.register(RealEstate, RealEstateAdmin)
admin.site.register(PropertyType)