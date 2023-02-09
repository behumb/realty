from rest_framework.routers import SimpleRouter
from .views import RealEstateViewSet


router = SimpleRouter()
router.register(r'real-estates', RealEstateViewSet, basename='real-estates')
urlpatterns = []
urlpatterns += router.urls