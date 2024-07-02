from rest_framework.viewsets import ModelViewSet
from .models import Divinity, Category, Hero, MythicalCreature
from .serializers import DivinityDetailSerializer, DivinityListSerializer, CategoryDetailSerializer, CategoryListSerializer, HeroDetailSerializer, HeroListSerializer, MythicalCreatureDetailSerializer, MythicalCreatureListSerializer

from django_filters.rest_framework import DjangoFilterBackend
from .filters import DivinityFilter, HeroFilter, MythicalCreatureFilter



class CategoryViewSet(ModelViewSet):
    serializer_class = CategoryListSerializer
    detail_serializer_class = CategoryDetailSerializer
    filter_backends = [DjangoFilterBackend]
    
    def get_queryset(self):
        return Category.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class() 
    


class DivinityViewSet(ModelViewSet):
    serializer_class = DivinityListSerializer
    detail_serializer_class = DivinityDetailSerializer
    
    def get_queryset(self):
        return Divinity.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class() 
    
    filter_backends= [DjangoFilterBackend]
    filterset_class = DivinityFilter


class HeroViewSet(ModelViewSet):
   serializer_class = HeroListSerializer
   detail_serializer_class = HeroDetailSerializer

   def get_queryset(self):
       return Hero.objects.all()
   
   def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class() 
    
   filter_backends = [DjangoFilterBackend]
   filterset_class = HeroFilter


class MythicalCreatureViewSet(ModelViewSet):
    serializer_class = MythicalCreatureListSerializer
    detail_serializer_class = MythicalCreatureDetailSerializer
    
    def get_queryset(self):
        return MythicalCreature.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class() 
    
        
    filter_backends = [DjangoFilterBackend]
    filterSet = MythicalCreatureFilter
    




