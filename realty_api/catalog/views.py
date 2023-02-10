from rest_framework import status, viewsets, mixins
from .models import RealEstate
from .serializers import RealEstateShortSerializer
from rest_framework import filters


class RealEstateViewSet(viewsets.ModelViewSet):
    serializer_class = RealEstateShortSerializer
    queryset = RealEstate.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['cost']
