from django import forms

from .models import Category, Divinity, Hero, MythicalCreature
from django.core.exceptions import ValidationError


class CategoryAdminForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = '__all__'

    def validate_name(self):
        name = self.cleaned_data['name']
        if Category.objects.filter(name=name).exists():
            raise ValidationError("Category already exists")
        return name
    
class UniqueNameAdminForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data['name']
        if self._meta.model.objects.filter(name=name).exists():
            raise ValidationError(f"{self._meta.model.__name__} with this name already exists")
        return name
    

class DivinityAdminForm(forms.ModelForm):
    
    class Meta:
        model = Divinity
        fields = '__all__'
    
    def validate_name(self):
        name = self.cleaned_data.get('name')
        if Divinity.objects.filter(name=name).exists():
            raise ValidationError('Divinity already exists')
        return name
    

class HeroAdminForm(forms.ModelForm):
    
    class Meta:
        model = Hero
        fields = '__all__'
    
    # def validate_name(self):
    #     name = self.cleaned_data['name']
    #     if Hero.objects.filter(name=name).exists():
    #         raise ValidationError('Hero already exists')
    #     return name
    # def validate_name(self, value):
    #     if Hero.objects.filter(name=value).exists():
    #         raise ValidationError('Hero aleady exists')
    #     return value
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Hero.objects.filter(name=name).exists():
            raise forms.ValidationError("A hero with this name already exists.")
        return name
        
    

class MythicalCreaturedminForm(forms.ModelForm):
    
    class Meta:
        model = MythicalCreature
        fields = '__all__'
    
    def validate_name(self):
        name = self.cleaned_data.get('name')
        if MythicalCreature.objects.filter(name=name).exists():
            raise ValidationError('Creature already exists')
        return name



