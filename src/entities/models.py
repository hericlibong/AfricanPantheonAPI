from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image
from .validator import UniqueNameMixin
from django.conf import settings




def validate_image(image):
     valid_mime_types = ['image/jpeg', 'image/png', 'image/gif', 'image/webp']
     file_mime_type = Image.open(image).get_format_mimetype()
     if file_mime_type not in valid_mime_types:
         raise ValidationError('Unsupported file type. ')
     

class Category(models.Model, UniqueNameMixin):
    name = models.CharField(max_length=100, help_text="Le nom de la categorie")
    description = models.TextField(max_length=100, help_text="Texte qui décrit la catégorie")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
        


    def __str__(self):
        return self.name


class Divinity(models.Model):
    name = models.CharField(max_length=100, help_text="Le nom principal de la divinité, y compris d'éventuels surnoms ou variantes régionales.")
    gender = models.CharField(max_length=1,default="M", choices = [('M', 'Male'), ('F', 'Female'), ('A', 'Androgyn')], 
                              help_text="Genre de la divinité. Elle peut être féminine, masculine, ou androgyne")
    domain = models.CharField(max_length=100, help_text="Les principaux domaines ou éléments associés à la divinité (e.g., tonnerre, amour, guerre).")
    main_symbol = models.CharField(max_length=100, help_text="Un élément ou objet principal associé à la divinité, tel qu'un animal, une plante, ou un objet spécifique.")
    associated_myths = models.TextField(help_text="Descriptions des mythes ou légendes les plus connus impliquant la divinité.")
    characteristics = models.TextField(help_text="Traits principaux ou aspects de la personnalité mythique, par exemple, vengeur, protecteur, sage.")
    manifestations = models.TextField(help_text="Descriptions des formes que la divinité peut prendre dans les récits mythologiques.")
    symbolic_animals = models.CharField(max_length=100, help_text="Animaux qui sont fréquemment liés à la divinité dans les mythes ou comme symboles.")
    power_objects = models.CharField(max_length=100, help_text="Objets mythiquement significatifs associés à la divinité, tels qu'une arme ou un artefact.")
    cultural_role = models.TextField(help_text="Description du rôle de la divinité dans la culture, par exemple, son influence sur l'art, la littérature, ou les pratiques sociales.")
    festivals = models.TextField(help_text="Mentions de festivals ou célébrations historiquement liés à la divinité, en se concentrant sur leur aspect culturel ou commémoratif.")
    country = models.CharField(max_length=50, blank=True, null=True, help_text="Pays actuel d'où est issue la divinité")
    origin = models.CharField(max_length=100, help_text="Région ou culture spécifique d'où la divinité est originaire.")
    ethnicity = models.CharField(max_length=100, help_text="Groupe ethnique principalement associé à la divinité.")
    image = models.ImageField(upload_to='divinity_images/', null=True, blank=True, validators=[validate_image], 
                              help_text="Champ pour stocker des images représentatives ou artistiques de la divinité.")
    image_caption = models.CharField(max_length=255, blank=True, null=True)
    parents = models.CharField(max_length=255, blank=True, null=True, help_text="Noms des parents de la divinité, si applicable.")
    descendants = models.CharField(max_length=255, blank=True, null=True, help_text="Noms des descendants de la divinité, si applicable.")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='divinity')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_divinities', null=True, blank=True, help_text="Utilisateur qui a créé la divinité.")
    

    # def validate_name(self):
    #     if Category.objects.filter(name=self.name).exists():
    #         raise ValidationError("Hero already exists")

    def __str__(self):
        return self.name

    
class Hero(models.Model, UniqueNameMixin):
    name = models.CharField(max_length=100, help_text="Le nom principal du héros.")
    gender = models.CharField(max_length=1, choices=[('M', 'Masculin'), ('F', 'Féminin'), ('A', 'Androgyne')], help_text="Le genre du héros.")
    story = models.TextField(help_text="L'histoire ou les légendes associées au héros.")
    titles = models.CharField(max_length=255, blank=True, null=True, help_text="Titres honorifiques ou noms alternatifs du héros.")
    achievements = models.TextField(blank=True, null=True, help_text="Réalisations notables ou exploits du héros.")
    enemies = models.TextField(blank=True, null=True, help_text="Ennemis ou adversaires du héros dans les mythes.")
    allies = models.TextField(blank=True, null=True, help_text="Alliés ou compagnons du héros dans les mythes.")
    country = models.CharField(max_length=100, blank=True, null=True, help_text="Le pays d'origine du héros.")
    origin = models.CharField(max_length=100, help_text="La région ou culture spécifique d'où le héros est originaire.")
    image = models.ImageField(upload_to='hero_images/', null=True, blank=True, validators=[validate_image], help_text="Champ pour stocker des images représentatives ou artistiques du héros.")
    image_caption = models.CharField(max_length=255, null=True, blank=True, help_text="Légende descriptive de l'image du héros.")
    parents = models.CharField(max_length=255, blank=True, null=True, help_text="Nom des parents du héros ou parents connus.")
    descendants = models.CharField(max_length=255, blank=True, null=True, help_text="Noms des descendants de du héros, si descendants connus.")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='heroes', help_text="Catégorie à laquelle appartient le héros.")
    date_created = models.DateTimeField(auto_now_add=True, help_text="Date de création du héros.")
    date_updated = models.DateTimeField(auto_now=True, help_text="Date de la dernière mise à jour du héros.")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_heroes', null=True, blank=True, help_text="Utilisateur qui a créé le héros.")

    def validate_name(self):
        if Category.objects.filter(name=self.name).exists():
            raise ValidationError("Hero already exists")

    def __str__(self):
        return self.name

    
class MythicalCreature(models.Model, UniqueNameMixin):
    name = models.CharField(max_length=100, help_text="Le nom principal de la créature mythique.")
    description = models.TextField(help_text="Description détaillée de la créature mythique.")
    country = models.CharField(max_length=100, help_text="Le pays d'origine de la créature mythique.")
    habitat = models.CharField(max_length=255, help_text="L'habitat naturel ou mythologique de la créature.")
    powers = models.TextField(help_text="Les pouvoirs ou capacités surnaturelles de la créature.")
    diet = models.CharField(max_length=255, blank=True, null=True, help_text="Régime alimentaire de la créature mythique.")
    size = models.CharField(max_length=100, blank=True, null=True, help_text="Taille ou dimensions typiques de la créature.")
    appareance = models.TextField(blank=True, null=True, help_text= "Brêve description de la créature. Mise en avant de ses attributs physiques")
    weaknesses = models.TextField(blank=True, null=True, help_text="Faiblesses ou vulnérabilités de la créature.")
    strengths = models.TextField(blank=True, null=True, help_text="Forces ou capacités spéciales de la créature.")
    image = models.ImageField(upload_to='creature_images/', null=True, blank=True, validators=[validate_image], help_text="Champ pour stocker des images représentatives ou artistiques de la créature.")
    image_caption = models.CharField(max_length=255, null=True, blank=True, help_text="Légende descriptive de l'image de la créature.")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='creatures', help_text="Catégorie à laquelle appartient la créature mythique.")
    date_created = models.DateTimeField(auto_now_add=True, help_text="Date de création de la créature.")
    date_updated = models.DateTimeField(auto_now=True, help_text="Date de la dernière mise à jour de la créature.")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_creatures', null=True, blank=True, help_text="Utilisateur qui a créé la créature.")

    def clean(self):
        if Category.objects.filter(name=self.name).exists():
            raise ValidationError("Creature name already exists")
        
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
  
    
