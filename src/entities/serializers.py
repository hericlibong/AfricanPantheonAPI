from rest_framework import serializers
from .validator import  ImageValidationMixin
from .models import Divinity, Category, Hero, MythicalCreature


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class DivinitySerializer(ImageValidationMixin, serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = Divinity
        fields = '__all__'


  
class HeroSerializer(ImageValidationMixin, serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Hero
        fields = '__all__'



class MythicalCreatureSerializer(ImageValidationMixin, serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = MythicalCreature
        fields = '__all__'



    

