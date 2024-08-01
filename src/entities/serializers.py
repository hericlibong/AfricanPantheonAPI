from rest_framework import serializers

from user_profiles.models import UserProfile
from .validator import ImageValidationMixin, CreatedByMixin
from .models import Divinity, Category, Hero, MythicalCreature, ImageWithCaption



# Dinivity serializers

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

class ApperanceSerializer(serializers.Serializer):
    gender = serializers.CharField(max_length=100, allow_blank=True)
    distincts_physicals_signs = serializers.ListField(child=serializers.CharField(max_length=100), allow_empty=True)

class IdentitySerializer(serializers.Serializer):
    cultural_role = serializers.CharField(max_length=255, allow_blank=True)
    pantheon = serializers.CharField(max_length=255, required = False, allow_blank=True)
    alignment = serializers.CharField(max_length=255, required = False, allow_blank=True)

class CategoryAssociationSerializer(serializers.Serializer):
    domain = serializers.ListField(child=serializers.CharField(max_length=100), allow_empty=True)
    main_symbol = serializers.ListField(child=serializers.CharField(max_length=100), allow_empty=True)

class DescriptionSerializer(serializers.Serializer):
    story_description = serializers.CharField(allow_blank=True)
    characteristics = serializers.ListField(child=serializers.CharField(max_length=100),allow_empty=True)
    manifestations = serializers.CharField(max_length=255, allow_blank=True)
    symbolic_animals = serializers.ListField(child=serializers.CharField(max_length=100), allow_empty=True)
    powers_objects = serializers.ListField(child=serializers.CharField(max_length=100), allow_empty=True)


class OriginNationlitySerializer(serializers.Serializer):
    country = serializers.CharField(max_length=100, allow_blank=True)
    origin = serializers.CharField(max_length=100, allow_blank=True)
    ethnicity = serializers.ListField(child=serializers.CharField(max_length=100), allow_empty=True)


class GenealogySerializer(serializers.Serializer):
    parents = serializers.ListField(child=serializers.CharField(max_length=100), allow_empty=True)
    descendants = serializers.ListField(child=serializers.CharField(max_length=100), allow_empty=True)
    conjoint = serializers.ListField(child=serializers.CharField(max_length=100), allow_empty=True)


class ImageWithCaptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageWithCaption
        fields = ['image', 'image_caption']



class DivinityDetailSerializer(CreatedByMixin, serializers.ModelSerializer):
    appearance = ApperanceSerializer(source='*')
    identity = IdentitySerializer(source='*')
    category_association = CategoryAssociationSerializer(source='*')
    description = DescriptionSerializer(source='*')
    origins_natinality = OriginNationlitySerializer(source='*')
    genealogy = GenealogySerializer(source='*')
    images = ImageWithCaptionSerializer(many=True, read_only=True)

    class Meta:
        model = Divinity
        fields = [
            'id', 'name', 'category', 'date_created', 'date_updated',  'created_by',
            'appearance', 'identity', 'category_association', 'description',
            'origins_natinality', 'genealogy', 'images'
        ]    


# Hero serializers

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
        

class HeroDetailSerializer(ImageValidationMixin, CreatedByMixin, serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    
    
    class Meta:
        model = Hero
        fields = '__all__'
        reda_only_fields = ['created_by']

    


class MythicalCreatureListSerializer(ImageValidationMixin, serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    created_by = serializers.StringRelatedField()

    class Meta:
        model = MythicalCreature
        fields = ['id', 'date_created', 'date_updated', 'name', 'appareance', 'habitat', 'country','image',
                  'category', 'created_by']
        
class MythicalCreatureDetailSerializer(ImageValidationMixin, CreatedByMixin, serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    
    
    class Meta:
        model = MythicalCreature
        fields = '__all__'
        reda_only_fields = ['created_by']

    


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
    

    

