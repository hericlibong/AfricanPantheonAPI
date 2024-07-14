from django.urls import path, include
from rest_framework import routers
from .views import UserProfileViewSet


router = routers.SimpleRouter()
router.register(r'profiles', UserProfileViewSet)


urlpatterns = [
    path('', include(router.urls))
]