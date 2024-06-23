
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.fields import CharField, TextField
import unicodedata
import re
from PIL import Image
from django.utils import timezone



def validate_image(image):
     valid_mime_types = ['image/jpeg', 'image/png', 'image/gif', 'image/webp']
     file_mime_type = Image.open(image).get_format_mimetype()
     if file_mime_type not in valid_mime_types:
         raise ValidationError('Unsupported file type. ')
     

class Category(models.Model):
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
    prompt = models.TextField(max_length=300, blank=True, null=True, help_text="Aggrégation des attributs pour composer le prompt de la génération de l'image du personnage")
    parents = models.CharField(max_length=255, blank=True, null=True, help_text="Noms des parents de la divinité, si applicable.")
    descendants = models.CharField(max_length=255, blank=True, null=True, help_text="Noms des descendants de la divinité, si applicable.")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @staticmethod
    def clean_input(text):
        if isinstance(text, str):
            # Normalisation Unicode
            text = unicodedata.normalize('NFKD', text)
            # Supprimer les caractères de contrôle
            text = ''.join(c for c in text if unicodedata.category(c) != 'Cc')
            # Supprimer les caractères non désirés spécifiques
            text = re.sub(r'[^\w\s\-.,;:!?\'"]+', '', text)
            # Supprimer les espaces supplémentaires
            text = re.sub(r'\s+', ' ', text)
            text = text.encode('utf-8', 'replace').decode('utf-8').strip()
        return text
   
    def save(self, *args, **kwargs):
        for field in self._meta.fields:
            if isinstance(field, (CharField, TextField)):
                original_value = getattr(self, field.name)
                cleaned_value = self.clean_input(original_value)
                if cleaned_value != original_value:
                    print(f"Cleaning {field.name}: '{original_value}' to '{cleaned_value}'")  # Log pour le débogage
                setattr(self, field.name, cleaned_value)
        super().save(*args, **kwargs)

class Hero(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=[('M', 'Masculin'), ('F', 'Féminin'), ('A', 'Androgyne')])
    story = models.TextField()
    country = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    image = models.ImageField(upload_to='hero_images/', null=True, blank=True)
    image_caption = models.CharField(max_length=255, null=True , blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='heroes')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
class MythicalCreature(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.CharField(max_length=100)
    habitat = models.CharField(max_length=255)
    powers = models.TextField()
    image = models.ImageField(upload_to='creature_images/', null=True, blank=True)
    image_caption = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='creatures')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name    
    
