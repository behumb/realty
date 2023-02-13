from rest_framework import status, viewsets, mixins, generics
from .models import RealEstate
from .serializers import RealEstateShortSerializer
from rest_framework import filters as rest_filters
from django_filters import rest_framework as filters


class NumberInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="cost", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="cost", lookup_expr='lte')
    min_square = filters.NumberFilter(field_name="total_square", lookup_expr='gte')
    max_square = filters.NumberFilter(field_name="total_square", lookup_expr='lte')
    bedrooms = filters.BaseInFilter(field_name="bedroom_count", lookup_expr='in')
    bathroom = filters.BaseInFilter(field_name="bathroom_count", lookup_expr='in')

    class Meta:
        model = RealEstate
        fields = ['property_type__name', 'location__city']


class RealEstateViewSet(generics.ListAPIView):
    queryset = RealEstate.objects.all()
    serializer_class = RealEstateShortSerializer
    filter_backends = (filters.DjangoFilterBackend, rest_filters.OrderingFilter)
    filterset_class = ProductFilter
    ordering_fields = ('cost',)
