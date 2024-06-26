import os
import json
from django.core.management.base import BaseCommand
from entities.models import Divinity, Hero, MythicalCreature, Category

class Command(BaseCommand):
    help = 'Load data into the database for various models'

    def add_arguments(self, parser):
        parser.add_argument('model', type=str, help='The model to load data for (divinity, hero, creature)')
        parser.add_argument('file_path', type=str, help='The file path of the JSON file containing the data')

    def handle(self, *args, **kwargs):
        model_name = kwargs['model']
        file_path = kwargs['file_path']
        
        if not os.path.isfile(file_path):
            self.stdout.write(self.style.ERROR(f'File "{file_path}" does not exist'))
            return

        self.stdout.write(self.style.SUCCESS(f'File "{file_path}" exists'))

        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
            model = None
            category_default = None

            if model_name == 'divinity':
                model = Divinity
                category_default = 'divinities'
            elif model_name == 'hero':
                model = Hero
                category_default = 'heroes'
            elif model_name == 'creature':
                model = MythicalCreature
                category_default = 'creatures'
            else:
                self.stdout.write(self.style.ERROR('Invalid model specified'))
                return

            for item in data:
                category_name = item.pop('category', category_default)
                if not category_name:
                    category_name = category_default
                category, created = Category.objects.get_or_create(name=category_name)
                
                item['category'] = category

                image_path = item.pop('image', None)

                instance, created = model.objects.get_or_create(name=item['name'], defaults=item)

                if not created:
                    for key, value in item.items():
                        setattr(instance, key, value)
                    instance.save()
                    self.stdout.write(self.style.WARNING(f'{instance.name} already exists in the database and was updated'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'{instance.name} has been added to the database'))
