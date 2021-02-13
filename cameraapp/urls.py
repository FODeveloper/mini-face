from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'positions', PositionViewSet)
router.register(r'cameras', CameraViewSet)


urlpatterns = [
    path('cameraapp/', include(router.urls)),
]

