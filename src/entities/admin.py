from django.contrib import admin
from .models import Divinity, Hero, MythicalCreature, Category
from .admin_forms import UniqueNameAdminForm


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = UniqueNameAdminForm
    list_display = ('name', 'description')
    fields = ('name', 'description', 'date_created', 'date_updated')
    # readonly_fields spécifie les champs en lecture seule dans le formulaire
    readonly_fields = ('date_created', 'date_updated')


@admin.register(Divinity)
class DivinityAdmin(admin.ModelAdmin):
    form = UniqueNameAdminForm
    list_display = ('name', 'domain', 'gender', 'created_by')
    search_fields = ('name', 'domain')
    readonly_fields = ('date_created', 'date_updated', 'created_by')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'domain', 'category', 'main_symbol', 'characteristics', 
              'manifestations', 'symbolic_animals', 'power_objects', 'cultural_role', 
              'country', 'origin', 'ethnicity', 'gender')
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
        (
            ('User Information'), {
                'fields': ('created_by', )
            }),  
    )
   

    def save_model(self, request, obj, form, change):
        """Set the user field automatically."""
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

    
  
    
@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    form = UniqueNameAdminForm
    list_display = ('name', 'gender', 'image')
    search_fields = ('name', '')
    readonly_fields = ('date_created', 'date_updated', 'created_by')
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
        (
            ('User Information'), {
                'fields': ('created_by', )
            }), 
    )

    def save_model(self, request, obj, form, change):
        """Set the user field automatically."""
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

    
@admin.register(MythicalCreature)
class MythicalCreatureAdmin(admin.ModelAdmin):
    form = UniqueNameAdminForm
    list_display = ('name', 'description', 'image')
    search_fields = ('name', '')
    readonly_fields = ('date_created', 'date_updated', 'created_by')
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
        (
            ('User Information'), {
                'fields': ('created_by', )
            }),  
    )

    def save_model(self, request, obj, form, change):
        """Set the user field automatically."""
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

    