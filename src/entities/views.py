from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Divinity, Category, Hero, MythicalCreature
from .serializers import DivinitySerializer, CategorySerializer, HeroSerializer, MythicalCreatureSerializer



class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    
    def get_queryset(self):
        return Category.objects.all()

class DivinityViewSet(ModelViewSet):
    serializer_class = DivinitySerializer
    
    def get_queryset(self):
        return Divinity.objects.all()

class HeroViewSet(ModelViewSet):
   serializer_class = HeroSerializer

   def get_queryset(self):
       return Hero.objects.all()
    
class MythicalCreatureViewSet(ModelViewSet):
    serializer_class = MythicalCreatureSerializer
    
    def get_queryset(self):
        return MythicalCreature.objects.all()
    




