from rest_framework import status, viewsets, mixins
from .models import RealEstate
from .serializers import RealEstateSerializer


class RealEstateViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = RealEstateSerializer
    queryset = RealEstate.objects.select_related('location').prefetch_related('options')
