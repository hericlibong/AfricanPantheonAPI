from django.urls import path, include
from rest_framework import routers
from .views import DivinityViewSet, HeroViewSet, CategoryViewSet, MythicalCreatureViewSet


router = routers.SimpleRouter()
router.register(r'divinities', DivinityViewSet, basename='divinity')
router.register(r'heroes', HeroViewSet, basename='hero')
router.register(r'creatures', MythicalCreatureViewSet, basename='creature')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls))
]