from django.test import TestCase
from entities.models import Divinity
from entities.serializers import DivinitySerializer
from django.core.files.uploadedfile import SimpleUploadedFile

class DivinityModelTests(TestCase):

    def test_clean_input(self):
        dirty_text = "Obatalá 😊 é o Senhor das cores!  "
        cleaned_text = Divinity.clean_input(dirty_text)
        expected_text = "Obatala e o Senhor das cores!"
        self.assertEqual(cleaned_text, expected_text, f"Expected: '{expected_text}', but got: '{cleaned_text}'")

    def test_divinity_creation_with_image(self):
        image = SimpleUploadedFile(name='oshun.webp', content=b'', content_type='webp')
        divinity = Divinity.objects.create(
            name='TestDivinity',
            domain='TestDomain',
            main_symbol='TestSymbol',
            associated_myths='TestMyths',
            characteristics='TestCharacteristics',
            manifestations='TestManifestations',
            symbolic_animals='TestAnimals',
            power_objects='TestObjects',
            cultural_role='TestRole',
            festivals='TestFestivals',
            country='TestCountry',
            origin='TestOrigin',
            ethnicity='TestEthnicity',
            image=image
        )
        self.assertEqual(divinity.name, 'TestDivinity')
        self.assertIsNotNone(divinity.image)

class DivinitySerializerTests(TestCase):

    def test_serializer_with_image(self):
        image = SimpleUploadedFile(name='oshun.webp', content=b'', content_type='webp')
        divinity_data = {
            'name': 'TestDivinity',
            'domain': 'TestDomain',
            'main_symbol': 'TestSymbol',
            'associated_myths': 'TestMyths',
            'characteristics': 'TestCharacteristics',
            'manifestations': 'TestManifestations',
            'symbolic_animals': 'TestAnimals',
            'power_objects': 'TestObjects',
            'cultural_role': 'TestRole',
            'festivals': 'TestFestivals',
            'country': 'TestCountry',
            'origin': 'TestOrigin',
            'ethnicity': 'TestEthnicity',
            'image': image
        }
        serializer = DivinitySerializer(data=divinity_data)
        self.assertTrue(serializer.is_valid())
