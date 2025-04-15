from rest_framework import routers
from .api import CarrosViewSet

router = routers.DefaultRouter()
router.register('api/carros', CarrosViewSet, 'carros')
urlpatterns = router.urls