from rest_framework import routers
from .api import HamburguesaViewSet

router = routers.DefaultRouter()
router.register('api/hamburguesas', HamburguesaViewSet, 'hamburguesas')
urlpatterns = router.urls