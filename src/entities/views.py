from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import Divinity, Category, Hero, MythicalCreature
from .serializers import (DivinityDetailSerializer, DivinityListSerializer, CategoryDetailSerializer, 
                          CategoryListSerializer, HeroDetailSerializer, HeroListSerializer, 
                          MythicalCreatureDetailSerializer, MythicalCreatureListSerializer)

from django_filters.rest_framework import DjangoFilterBackend
from .filters import DivinityFilter, HeroFilter, MythicalCreatureFilter

class MultipleSerializerMixin:
    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return self.serializer_class


class AdminCategoryViewSet(MultipleSerializerMixin, ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    detail_serializer_class = CategoryDetailSerializer
    filter_backends = [DjangoFilterBackend]

class AdminDivinityViewSet(MultipleSerializerMixin, ModelViewSet):
    queryset = Divinity.objects.all()
    serializer_class = DivinityDetailSerializer
    detail_serializer_class = DivinityDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DivinityFilter

class AdminHeroViewSet(MultipleSerializerMixin, ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroListSerializer
    detail_serializer_class = HeroDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HeroFilter


class CategoryViewSet(MultipleSerializerMixin, ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    detail_serializer_class = CategoryDetailSerializer
    filter_backends = [DjangoFilterBackend]
    
    
    
class DivinityViewSet(MultipleSerializerMixin, ReadOnlyModelViewSet):
    queryset = Divinity.objects.all()
    serializer_class = DivinityListSerializer
    detail_serializer_class = DivinityDetailSerializer
    filter_backends= [DjangoFilterBackend]
    filterset_class = DivinityFilter


class HeroViewSet(MultipleSerializerMixin, ReadOnlyModelViewSet):
   queryset = Hero.objects.all()
   serializer_class = HeroListSerializer
   detail_serializer_class = HeroDetailSerializer
   filter_backends = [DjangoFilterBackend]
   filterset_class = HeroFilter


class MythicalCreatureViewSet(MultipleSerializerMixin, ReadOnlyModelViewSet):
    queryset = MythicalCreature.objects.all()
    serializer_class = MythicalCreatureListSerializer
    detail_serializer_class = MythicalCreatureDetailSerializer  
    filter_backends = [DjangoFilterBackend]
    filterSet = MythicalCreatureFilter
    




