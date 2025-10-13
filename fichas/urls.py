from rest_framework.routers import DefaultRouter

from .views.ficha_viewset import FichaViewSet

router = DefaultRouter()
router.register(r"fichas", FichaViewSet, basename="ficha")

urlpatterns = router.urls
