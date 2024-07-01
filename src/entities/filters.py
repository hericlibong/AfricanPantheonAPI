# filters.py

import django_filters
from django_filters import FilterSet
from .models import Divinity, Hero, MythicalCreature

class DivinityFilter(FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', label='Name contains', help_text='Filter by name (contains)')
    gender = django_filters.ChoiceFilter(field_name='gender', choices=[('M', 'Male'), ('F', 'Female'), ('A', 'Androgyn')], label='Gender', help_text='Filter by gender')
    country = django_filters.CharFilter(field_name='country', lookup_expr='icontains', label='Country contains', help_text='Filter by country (contains)')
    origin = django_filters.CharFilter(field_name='origin', lookup_expr='icontains', label='Origin contains', help_text='Filter by origin (contains)')
    category__name = django_filters.CharFilter(field_name='category__name', lookup_expr='exact', label='Category name', help_text='Filter by category name')

    class Meta:
        model = Divinity
        fields = ['name', 'gender', 'country', 'origin', 'category__name']

class HeroFilter(FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', label='Name contains', help_text='Filter by name (contains)')
    gender = django_filters.ChoiceFilter(field_name='gender', choices=[('M', 'Male'), ('F', 'Female'), ('A', 'Androgyn')], label='Gender', help_text='Filter by gender')
    country = django_filters.CharFilter(field_name='country', lookup_expr='icontains', label='Country contains', help_text='Filter by country (contains)')
    origin = django_filters.CharFilter(field_name='origin', lookup_expr='icontains', label='Origin contains', help_text='Filter by origin (contains)')
    category__name = django_filters.CharFilter(field_name='category__name', lookup_expr='exact', label='Category name', help_text='Filter by category name')

    class Meta:
        model = Hero
        fields = ['name', 'gender', 'country', 'origin', 'category__name']

class MythicalCreatureFilter(FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', label='Name contains', help_text='Filter by name (contains)')
    country = django_filters.CharFilter(field_name='country', lookup_expr='icontains', label='Country contains', help_text='Filter by country (contains)')
    habitat = django_filters.CharFilter(field_name='habitat', lookup_expr='icontains', label='Habitat contains', help_text='Filter by habitat (contains)')
    category__name = django_filters.CharFilter(field_name='category__name', lookup_expr='exact', label='Category name', help_text='Filter by category name')

    class Meta:
        model = MythicalCreature
        fields = ['name', 'country', 'habitat', 'category__name']
