import django_filters

from .models import Divinity, Hero, MythicalCreature



class DivinityFilter(django_filters.FilterSet):
    class Meta:
        model = Divinity
        fields = {
            'name':['exact', 'icontains'],
            'gender':['exact'],
            'country':['exact', 'icontains'],
            'origin': ['exact', 'icontains'],
            'category__name':['exact']
        }

class HeroFilter(django_filters.FilterSet):
    class Meta:
        model = Hero
        fields = {
            'name':['exact', 'icontains'],
            'gender':['exact'],
            'country':['exact', 'icontains'],
            'origin': ['exact', 'icontains'],
            'category__name':['exact']
        }


class MythicalCreatureFilter(django_filters.FilterSet):
    class Meta:
        model = MythicalCreature
        fields = {
            'name':['exact', 'icontains'],
            'country':['exact', 'icontains'],
            'habitat': ['exact', 'icontains'],
            'category__name':['exact']
        }


