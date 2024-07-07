from django.contrib import admin
from .models import Divinity, Hero, MythicalCreature, Category
from .admi_forms import CategoryAdminForm, DivinityAdminForm, HeroAdminForm, MythicalCreaturedminForm, UniqueNameAdminForm


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # form = CategoryAdminForm
    form = UniqueNameAdminForm
    list_display = ('name', 'description')
    fields = ('name', 'description', 'date_created', 'date_updated')
    # readonly_fields spécifie les champs en lecture seule dans le formulaire
    readonly_fields = ('date_created', 'date_updated')



@admin.register(Divinity)
class DivinityAdmin(admin.ModelAdmin):
    form = DivinityAdminForm
    list_display = ('name', 'domain', 'gender', 'image')
    search_fields = ('name', 'domain')
    readonly_fields = ('date_created', 'date_updated')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'domain', 'category', 'main_symbol', 'associated_myths', 'characteristics', 
              'manifestations', 'symbolic_animals', 'power_objects', 'cultural_role', 
              'festivals', 'country', 'origin', 'ethnicity', 'gender')
        }),
        ('Image Information', {
            'fields':('image', 'image_caption')
        }),
        ('Family', {
            'fields':('parents', 'descendants')
        }),
        ('Date Information', {
            'fields':('date_created', 'date_updated')
        }),  
    )
    def date_created(self, obj):
        return obj.date_created
    
    def date_updated(self, obj):
        return obj.date_updated
    

  

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    form = HeroAdminForm
    list_display = ('name', 'gender', 'image')
    search_fields = ('name', '')
    readonly_fields = ('date_created', 'date_updated')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'gender', 'story', 'titles', 'achievements', 'enemies', 'allies', 
              'country', 'origin', 'category')        
    }),
        ('Image Information', {
            'fields':('image', 'image_caption')
        }),
        ('Family', {
            'fields':('parents', 'descendants')
        }),
        ('Date Information', {
            'fields':('date_created', 'date_updated')
        }),  
    )

    def date_created(self, obj):
        return obj.date_created
    
    def date_updated(self, obj):
        return obj.date_updated
    
@admin.register(MythicalCreature)

class MythicalCreatureAdmin(admin.ModelAdmin):
    form = MythicalCreaturedminForm
    list_display = ('name', 'description', 'image')
    search_fields = ('name', '')
    # fields = ('name', 'description', 'country', 'habitat', 
    #           'powers', 'diet', 'size','appareance', 'weaknesses', 'strengths', 'image', 'image_caption', 'category',
    #           'date_created', 'date_updated')
    readonly_fields = ('date_created', 'date_updated')

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'country', 'habitat', 
              'powers', 'diet', 'size','appareance', 'weaknesses', 'strengths', 'category')        
    }),
        ('Image Information', {
            'fields':('image', 'image_caption')
        }),
        ('Date Information', {
            'fields':('date_created', 'date_updated')
        }),  
    )

    def date_created(self, obj):
        return obj.date_created
    
    def date_updated(self, obj):
        return obj.date_updated



