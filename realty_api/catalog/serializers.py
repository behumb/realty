from rest_framework.serializers import ModelSerializer
from .models import RealEstate, Location


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = ('address', 'state', 'latitude', 'longitude',)


class RealEstateShortSerializer(ModelSerializer):
    class Meta:
        model = RealEstate
        fields = (
            'id',
            'name',
            'description',
            'get_image',
            'cost',
        )


class RealEstateSerializer(ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = RealEstate
        fields = (
            'id',
            'name',
            'description',
            'get_image',
            'location',
        )
