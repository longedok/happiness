from django.urls import path, include

from server.apps.main.views import index

app_name = 'main'

urlpatterns = [
    path('api/', include("server.apps.words.urls")),
    path('hello/', index, name='hello'),
]
