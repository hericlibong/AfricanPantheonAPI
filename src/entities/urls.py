from django.urls import path, include
from rest_framework import routers
from .views import(DivinityViewSet, HeroViewSet, CategoryViewSet, 
                   MythicalCreatureViewSet, AdminCategoryViewSet, AdminDivinityViewSet, AdminHeroViewSet)


router = routers.SimpleRouter()
router.register(r'divinities', DivinityViewSet, basename='divinity')
router.register(r'heroes', HeroViewSet, basename='hero')
router.register(r'creatures', MythicalCreatureViewSet, basename='creature')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'admin/categories', AdminCategoryViewSet, basename='admin-categories')
router.register(r'admin/divinities', AdminDivinityViewSet, basename='admin-divinity')
router.register(r'admin/heroes', AdminHeroViewSet, basename='admin-heroes')

urlpatterns = [
    path('', include(router.urls))
]