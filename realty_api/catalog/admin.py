from django.contrib import admin
from .models import RealEstate, Option, Location
from nested_inline.admin import NestedStackedInline, NestedModelAdmin


class LocationInline(NestedStackedInline):
    model = Location
    extra = 1
    fk_name = 'real_estate'


class OptionInline(NestedStackedInline):
    model = Option
    extra = 1
    fk_name = 'real_estate'


class RealEstateAdmin(NestedModelAdmin):
    model = RealEstate
    inlines = [OptionInline, LocationInline]


admin.site.register(RealEstate, RealEstateAdmin)
