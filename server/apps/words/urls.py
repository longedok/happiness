from rest_framework.routers import DefaultRouter

from server.apps.words.api.word import WordViewSet

app_name = "words"

router = DefaultRouter()
router.register("words", WordViewSet)


urlpatterns = router.urls
