from rest_framework.routers import DefaultRouter

from server.words.api.word import WordViewSet

router = DefaultRouter()
router.register("words", WordViewSet)


urlpatterns = router.urls
