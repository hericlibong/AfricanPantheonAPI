from rest_framework import serializers
from .validator import ImageValidationMixin
from .models import Divinity, Category, Hero, MythicalCreature


class DivinitySerializer(ImageValidationMixin, serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    
    class Meta:
        model = Divinity
        fields = '__all__'

class HeroSerializer(ImageValidationMixin, serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    
    class Meta:
        model = Hero
        fields = '__all__'

class MythicalCreatureSerializer(ImageValidationMixin, serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    
    class Meta:
        model = MythicalCreature
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    divinity = serializers.SerializerMethodField()
    heroes = serializers.SerializerMethodField()
    creatures = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_divinity(self, instance):
        queryset = instance.divinity.all()
        serializer = DivinitySerializer(queryset, many=True)
        return serializer.data
    
    def get_heroes(self, instance):
        queryset = instance.heroes.all()
        serializer = HeroSerializer(queryset, many=True)
        return serializer.data 
    
    def get_creatures(self, instance):
        queryset = instance.creatures.all()
        serializer = MythicalCreatureSerializer(queryset, many=True)
        return serializer.data
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        filtered_representation = {key: value for key, value in representation.items() if value != []}
        return filtered_representation
    

    

