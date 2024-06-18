from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DivinityViewSet


router = DefaultRouter()
router.register(r'divinities', DivinityViewSet)

urlpatterns = [
    path('', include(router.urls))
]