import os
import json
from django.core.management.base import BaseCommand
from entities.models import Divinity

class Command(BaseCommand):
    help = 'Load divinities data into the database'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The file path of the JSON file containing the divinity data')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        if not os.path.isfile(file_path):
            self.stdout.write(self.style.ERROR(f'File "{file_path}" does not exist'))
            return
        
        self.stdout.write(self.style.SUCCESS(f'File "{file_path}" exists'))
        
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                image_path = item.pop('image', None)  # Ignore the image field
                instance, created = Divinity.objects.get_or_create(name=item['name'], defaults=item)
                
                if not created:
                    for key, value in item.items():
                        setattr(instance, key, value)
                    instance.save()
                    self.stdout.write(self.style.WARNING(f'{instance.name} already exists in the database and was updated'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'{instance.name} has been added to the database'))
