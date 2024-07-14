from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import Divinity, Category, Hero, MythicalCreature
from .serializers import (DivinityDetailSerializer, DivinityListSerializer, CategoryDetailSerializer, 
                          CategoryListSerializer, HeroDetailSerializer, HeroListSerializer, 
                          MythicalCreatureDetailSerializer, MythicalCreatureListSerializer)
from django_filters.rest_framework import DjangoFilterBackend
from .filters import DivinityFilter, HeroFilter, MythicalCreatureFilter


class MultipleSerializerMixin:
    """A mixin that allows you to have different serializers for different actions."""
    detail_serializer_class = None

    def get_serializer_class(self):
        """Return the class to use for the serializer."""
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return self.serializer_class
    
class UserCreatedMixin:
    """A mixin that allows you to set the user field automatically."""
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class AdminCategoryViewSet(MultipleSerializerMixin, ModelViewSet):
    """A viewset for viewing and editing category instances."""
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    detail_serializer_class = CategoryDetailSerializer
    filter_backends = [DjangoFilterBackend]


class AdminDivinityViewSet(MultipleSerializerMixin, ModelViewSet, UserCreatedMixin):
    """A viewset for viewing and editing divinity instances."""
    queryset = Divinity.objects.all()
    serializer_class = DivinityDetailSerializer
    detail_serializer_class = DivinityDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DivinityFilter


class AdminHeroViewSet(MultipleSerializerMixin, ModelViewSet, UserCreatedMixin):
    """A viewset for viewing and editing hero instances."""
    queryset = Hero.objects.all()
    serializer_class = HeroListSerializer
    detail_serializer_class = HeroDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HeroFilter


class CategoryViewSet(MultipleSerializerMixin, ReadOnlyModelViewSet):
    """A viewset for viewing category instances."""
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    detail_serializer_class = CategoryDetailSerializer
    filter_backends = [DjangoFilterBackend]
    
       
class DivinityViewSet(MultipleSerializerMixin, ReadOnlyModelViewSet, UserCreatedMixin):
    """A viewset for viewing divinity instances."""
    queryset = Divinity.objects.all()
    serializer_class = DivinityListSerializer
    detail_serializer_class = DivinityDetailSerializer
    filter_backends= [DjangoFilterBackend]
    filterset_class = DivinityFilter


class HeroViewSet(MultipleSerializerMixin, ReadOnlyModelViewSet, UserCreatedMixin):
   """A viewset for viewing hero instances."""
   queryset = Hero.objects.all()
   serializer_class = HeroListSerializer
   detail_serializer_class = HeroDetailSerializer
   filter_backends = [DjangoFilterBackend]
   filterset_class = HeroFilter


class MythicalCreatureViewSet(MultipleSerializerMixin, ReadOnlyModelViewSet, UserCreatedMixin):
    """A viewset for viewing mythical creature instances."""
    queryset = MythicalCreature.objects.all()
    serializer_class = MythicalCreatureListSerializer
    detail_serializer_class = MythicalCreatureDetailSerializer  
    filter_backends = [DjangoFilterBackend]
    filterSet = MythicalCreatureFilter
    




