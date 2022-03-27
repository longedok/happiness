from rest_framework.routers import DefaultRouter

from server.core.api.word import WordViewSet

router = DefaultRouter()
router.register("words", WordViewSet)


urlpatterns = router.urls
