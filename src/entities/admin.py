from django.contrib import admin
from .models import Divinity, Hero, MythicalCreature, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    fields = ('name', 'description')
    # readonly_fields spécifie les champs en lecture seule dans le formulaire
    readonly_fields = ('date_created', 'date_updated')



@admin.register(Divinity)
class DivinityAdmin(admin.ModelAdmin):
    # list_display spécifie les champs à afficher dans la liste des objets du modèle
    list_display = ('name', 'domain', 'gender', 'image')
    
    # search_fields spécifie les champs sur lesquels il est possible de faire des recherches
    search_fields = ('name', 'domain')
    
    # fields spécifie l'ordre et les champs à afficher dans le formulaire d'ajout/modification
    fields = ('name', 'domain', 'main_symbol', 'associated_myths', 'characteristics', 
              'manifestations', 'symbolic_animals', 'power_objects', 'cultural_role', 
              'festivals', 'country', 'origin', 'ethnicity', 'gender', 'image', 'image_caption',
              'prompt', 'parents', 'descendants')
    
    # readonly_fields spécifie les champs en lecture seule dans le formulaire
    readonly_fields = ('created_at', 'updated_at')

    # Méthodes supplémentaires pour afficher les champs en lecture seule
    def created_at(self, obj):
        return obj.created_at

    def updated_at(self, obj):
        return obj.updated_at

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'image')
    search_fields = ('name', '')
    fields = ('name', 'gender', 'story', 'country', 'origin', 'image', 'image_caption',
              'category','date_created', 'date_updated')
    readonly_fields = ('date_created', 'date_updated')

    def date_created(self, obj):
        return obj.date_created
    
    def date_updated(self, obj):
        return obj.date_updated
    
@admin.register(MythicalCreature)
class MythicalCreatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')
    search_fields = ('name', '')
    fields = ('name', 'description', 'country', 'habitat', 
              'powers', 'image', 'image_caption', 'category',
              'date_created', 'date_updated')
    readonly_fields = ('date_created', 'date_updated')

    def date_created(self, obj):
        return obj.date_created
    
    def date_updated(self, obj):
        return obj.date_updated



