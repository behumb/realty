from rest_framework.serializers import ModelSerializer
from .models import Option, RealEstate, Location


class OptionSerializer(ModelSerializer):
    class Meta:
        model = Option
        fields = ('value', )


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = ('address', 'state', 'latitude', 'longitude',)


class RealEstateSerializer(ModelSerializer):
    options = OptionSerializer(many=True)
    location = LocationSerializer()

    class Meta:
        model = RealEstate
        fields = '__all__'
