from rest_framework import serializers
from .validator import ImageValidationMixin
from .models import Divinity, Category, Hero, MythicalCreature



class DivinityListSerializer(ImageValidationMixin, serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Divinity
        fields = ['id', 'date_created', 'date_updated', 'name', 
                  'gender', 'cultural_role', 'country', 'image', 'category']


class DivinityDetailSerializer(ImageValidationMixin, serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    
    class Meta:
        model = Divinity
        fields = '__all__'


class HeroListSerializer(ImageValidationMixin, serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Hero
        fields = ['id', 'date_created', 'date_updated', 'name','titles', 'gender',
                  'country', 'image', 'category']
        

class HeroDetailSerializer(ImageValidationMixin, serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    
    class Meta:
        model = Hero
        fields = '__all__'


class MythicalCreatureListSerializer(ImageValidationMixin, serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = MythicalCreature
        fields = ['id', 'date_created', 'date_updated', 'name', 'appareance', 'habitat', 'country',
                  'category']
        
class MythicalCreatureDetailSerializer(ImageValidationMixin, serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    
    class Meta:
        model = MythicalCreature
        fields = '__all__'



class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name']

class CategoryDetailSerializer(serializers.ModelSerializer):
    divinity = serializers.SerializerMethodField()
    heroes = serializers.SerializerMethodField()
    creatures = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_divinity(self, instance):
        queryset = instance.divinity.all()
        serializer = DivinityDetailSerializer(queryset, many=True)
        return serializer.data
    
    def get_heroes(self, instance):
        queryset = instance.heroes.all()
        serializer = HeroDetailSerializer(queryset, many=True)
        return serializer.data 
    
    def get_creatures(self, instance):
        queryset = instance.creatures.all()
        serializer = MythicalCreatureDetailSerializer(queryset, many=True)
        return serializer.data
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        filtered_representation = {key: value for key, value in representation.items() if value != []}
        return filtered_representation
    

    

