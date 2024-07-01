from rest_framework.viewsets import ModelViewSet
from .models import Divinity, Category, Hero, MythicalCreature
from .serializers import DivinitySerializer, CategorySerializer, HeroSerializer, MythicalCreatureSerializer

from django_filters.rest_framework import DjangoFilterBackend
from .filters import DivinityFilter, HeroFilter, MythicalCreatureFilter



class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    
    def get_queryset(self):
        return Category.objects.all()

class DivinityViewSet(ModelViewSet):
    serializer_class = DivinitySerializer
    
    def get_queryset(self):
        return Divinity.objects.all()
    
    filter_backends= [DjangoFilterBackend]
    filterset_class = DivinityFilter


class HeroViewSet(ModelViewSet):
   serializer_class = HeroSerializer

   def get_queryset(self):
       return Hero.objects.all()
    
   filter_backends = [DjangoFilterBackend]
   filterset_class = HeroFilter
    
class MythicalCreatureViewSet(ModelViewSet):
    serializer_class = MythicalCreatureSerializer
    
    def get_queryset(self):
        return MythicalCreature.objects.all()
    
    filter_backends = [DjangoFilterBackend]
    filterSet = MythicalCreatureFilter
    




