from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EbookViewSet, AudioFileViewSet

router = DefaultRouter()
router.register('ebooks', EbookViewSet)
router.register('audiofiles', AudioFileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
