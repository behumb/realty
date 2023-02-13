from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import RealEstateViewSet


router = SimpleRouter()
# router.register(r'real-estates', RealEstateViewSet.as_view(), basename='real-estates')
urlpatterns = [
    path('real-estates/', RealEstateViewSet.as_view())
]
urlpatterns += router.urls