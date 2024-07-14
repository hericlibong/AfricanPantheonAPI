from rest_framework import serializers

from user_profiles.models import UserProfile
from .validator import ImageValidationMixin
from .models import Divinity, Category, Hero, MythicalCreature



class DivinityListSerializer(ImageValidationMixin, serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Divinity
        fields = ['id', 'date_created', 'date_updated', 'name', 
                  'gender', 'cultural_role', 'country', 'image', 'category', 'created_by']
    
    def validate_name(self, value):
        if Category.objects.filter(name=value).exists():
            raise serializers.ValidationError("Divnity already exists")
        return value


class DivinityDetailSerializer(ImageValidationMixin, serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    created_by = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all(), required=False)
    
    class Meta:
        model = Divinity
        fields = '__all__'


class HeroListSerializer(ImageValidationMixin, serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Hero
        fields = ['id', 'date_created', 'date_updated', 'name','titles', 'gender',
                  'country', 'image', 'category', 'created_by']
    
    def validate_name(self, value):
        if Hero.objects.filter(name=value).exists():
            raise serializers.ValidationError('Hero aleady exists')
        return value
        

class HeroDetailSerializer(ImageValidationMixin, serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    created_by = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all(), required=False)
    
    class Meta:
        model = Hero
        fields = '__all__'


class MythicalCreatureListSerializer(ImageValidationMixin, serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    created_by = serializers.StringRelatedField()

    class Meta:
        model = MythicalCreature
        fields = ['id', 'date_created', 'date_updated', 'name', 'appareance', 'habitat', 'country','image',
                  'category', 'created_by']
        
class MythicalCreatureDetailSerializer(ImageValidationMixin, serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    created_by = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all(), required=False)
    
    class Meta:
        model = MythicalCreature
        fields = '__all__'



class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name', 'description']

    def validate_name(self, value):
        if Category.objects.filter(name=value).exists():
            raise serializers.ValidationError("Category already exists")
        return value 
    
    def validate(data):
        if data['name'] not in data['description']:
            raise serializers.ValidationError('Category name must be in description')
        return data



class CategoryDetailSerializer(serializers.ModelSerializer):
    divinity = DivinityListSerializer(many=True, read_only=True)
    heroes = HeroListSerializer(many=True, read_only=True)
    creatures = MythicalCreatureListSerializer(many=True, read_only=True)

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
    

    

