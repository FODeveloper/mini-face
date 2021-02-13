from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'detectedpersons', DetectedPersonViewSet)
router.register(r'snapshots', SnapShotViewSet)


urlpatterns = [
    path('alertapp/', include(router.urls)),
]
