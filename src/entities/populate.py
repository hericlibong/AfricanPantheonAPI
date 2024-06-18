import os
import django
from entities.models import Divinity

# Configuration de l'environnement Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "africanpantheon.settings")
django.setup()

# Fonction pour ajouter des données dans un modèle spécifique
def add_data(model, data):
    instance, created = model.objects.get_or_create(name=data['name'], defaults=data)
    if created:
        print(f"{model.__name__} {instance.name} a été ajoutée avec succès à la base de données.")
    else:
        print(f"{model.__name__} {instance.name} existe déjà dans la base de données.")

# Données de la divinité
divinity_data = {
    "name": "Obatala",
    "domain": "Pureté spirituelle, sagesse, éthique, création de l'humanité",
    "main_symbol": "Colombe blanche, bâton d'argent (opaxoro), robe blanche, coquilles de cauris",
    "associated_myths": "Création de la terre et des humains; Conflit avec Oduduwa; Mythe de la création où il a accidentellement introduit des imperfections chez les humains à cause de l'ivresse",
    "characteristics": "Sage, réfléchi, capable d'admettre ses erreurs, protecteur des personnes handicapées",
    "manifestations": "Peut prendre la forme d'une colombe blanche, souvent représenté en tenue blanche",
    "symbolic_animals": "Colombe blanche, escargot, chèvre blanche",
    "power_objects": "Bâton d'argent, chaîne d'argent utilisée pour descendre du ciel",
    "cultural_role": "Père de tous les orishas, créateur de l'humanité, consulté pour résoudre les conflits entre les orishas, vénéré dans plusieurs religions dérivées du culte Yoruba",
    "festivals": "Rituel annuel au Brésil (Candomblé) et dans la Santería afro-cubaine",
    "country": "Nigeria",
    "origin": "Yoruba (Nigeria)",
    "ethnicity": "Yoruba",
    "image": None,
    "parents": None,
    "descendants": None
}

# Exécution de la fonction d'ajout de données
if __name__ == "__main__":
    add_data(Divinity, divinity_data)
