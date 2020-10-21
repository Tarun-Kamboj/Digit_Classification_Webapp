from .views import DigitViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'digits', DigitViewSet)
urlpatterns = router.urls