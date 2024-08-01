from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import ArrayField
from PIL import Image
from .validator import UniqueNameMixin
from django.conf import settings


def validate_image(image):
     """Validate that the uploaded file is an image."""
     valid_mime_types = ['image/jpeg', 'image/png', 'image/gif', 'image/webp']
     file_mime_type = Image.open(image).get_format_mimetype()
     if file_mime_type not in valid_mime_types:
         raise ValidationError('Unsupported file type. ')
     
def upload_to(instance, filename, entity_type):
    """Generate a unique path for uploaded images."""
    return f'{entity_type}/{instance.id}/{filename}'
     

class Category(models.Model, UniqueNameMixin):
    """Model representing a category of entities."""
    name = models.CharField(max_length=100, help_text="Le nom de la categorie")
    description = models.TextField(max_length=100, help_text="Texte qui décrit la catégorie")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ImageWithCaption(models.Model):
    """Model to store images with captions."""
    image = models.ImageField(upload_to=upload_to, 
                              null=True, 
                              blank=True, 
                              validators=[validate_image], 
                              help_text="Champ pour stocker des images représentatives ou artistiques de la créature.")
    image_caption = models.CharField(max_length=255, 
                                     null=True, 
                                     blank=True, 
                                     help_text="Légende descriptive de l'image de la créature.")
   

    def __str__(self):
        return self.image_caption or 'no caption'
    

class Divinity(models.Model, UniqueNameMixin):
    name = models.CharField(max_length=100, help_text="The main name of the deity, including any nicknames or regional variants.")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='divinities', help_text="The category to which the deity belongs.")
    date_created = models.DateTimeField(auto_now_add=True, help_text="The date the deity was created.")
    date_updated = models.DateTimeField(auto_now=True, help_text="The date the deity was last updated.")	
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_divinities', null=True, blank=True, help_text="The user who created the deity.")

    # Appareance
    gender = models.CharField(max_length=1, choices=[('M', 'Man'), ('F', 'Female'), ('A', 'Androgyn')],
                            help_text="The gender of the divinity")
    distincts_physicals_signs = ArrayField(models.CharField(max_length=100), blank=True, null=True, 
                                                  help_text='Distinct physical signs or attributes of the deity. Ex : "turbaned", "masqued", "with a spear", "white beard"')
    # Identity
    cultural_role = models.CharField(max_length=100, help_text="Description of the deity's role in the culture, e.g., 'God of Thunder' , 'goddess of love', etc.")
    pantheon = models.CharField(max_length=100, blank=True, null=True, help_text="The pantheon or group of deities to which the deity belongs.")
    alignment = models.CharField(max_length=100, blank=True, null=True, help_text="The moral or ethical alignment of the deity, e.g., good, evil, neutral.")

    # Categories and Associations
    domain = ArrayField(models.CharField(max_length=100), blank=True, null=True,  help_text="The main domains or elements associated with the deity, e.g., thunder, love, war.")
    main_symbol = ArrayField(models.CharField(max_length=100), blank=True, null=True, help_text="A main element or object associated with the deity, such as an animal, plant, or specific object.")

    # Description
    story_description = models.TextField(blank=True, null=True, help_text="Description of the deity's story or mythological background.")
    characteristics = ArrayField(models.CharField(max_length=100), blank=True, null=True, help_text="Main traits or aspects of the mythical personality, e.g., vengeful, protective, wise.")
    manifestations = models.CharField(max_length=255, blank=True, null=True, 
                                      help_text="Descriptions of the forms the deity can take in mythological narratives. e.g: 'beautiful woman wearing jewelry' or 'man often depicted in white outfit'.")
    symbolic_animals = ArrayField(models.CharField(max_length=100), blank=True, null=True, help_text="Animals that are frequently linked to the deity in myths or as symbols.")
    power_objects = ArrayField(models.CharField(max_length=100), blank=True, null=True, help_text="Mythically significant objects associated with the deity, such as a weapon or artifact.")

    # Origins and Nationality
    country = models.CharField(max_length=50, blank=True, null=True, help_text="Current country from which the deity originates.")
    origin = models.CharField(max_length=100, blank=True, null=True, help_text="Specific region or culture from which the deity originates.")
    ethnicity = ArrayField(models.CharField(max_length=100), blank=True, null=True, help_text="Ethnic(s) group(s) primarily associated with the deity.")

    # Genealogy
    parents = ArrayField(models.CharField(max_length=100), blank=True, null=True, help_text="Names of the deity's parents, if applicable.")
    descendants = ArrayField(models.CharField(max_length=100), blank=True, null=True, help_text="Names of the deity's descendants, if applicable.")
    conjoint = ArrayField(models.CharField(max_length=100), blank=True, null=True, help_text="Name of the deity's spouse or partner, if applicable.")

    # Images
    images = models.ManyToManyField(ImageWithCaption, blank=True, related_name='divinities', help_text="Field to store representative or artistic images of the deity.")

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
  
    
