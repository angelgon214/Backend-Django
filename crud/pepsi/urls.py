from rest_framework import routers
from .api import PepsiViewSet

router = routers.DefaultRouter()
router.register('api/pepsi', PepsiViewSet, 'pepsi')
urlpatterns = router.urls
