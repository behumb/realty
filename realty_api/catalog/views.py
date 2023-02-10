from rest_framework import status, viewsets, mixins
from .models import RealEstate
from .serializers import RealEstateShortSerializer


class RealEstateViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = RealEstateShortSerializer
    queryset = RealEstate.objects.select_related('location').prefetch_related('options')
