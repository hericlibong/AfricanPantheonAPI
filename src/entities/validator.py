from PIL import Image
from django.core.exceptions import ValidationError
from rest_framework import serializers

class ImageValidationMixin:
    def validate_image(self, image):
        valid_mime_types = ['image/jpeg', 'image/png', 'image/gif', 'image/webp']
        try:
            file_mime_type = Image.open(image).get_format_mimetype()
            if file_mime_type not in valid_mime_types:
                raise ValidationError('Unsupported file type.')
        except Exception as e:
            raise ValidationError(f'Invalid image: {str(e)}')
        return image
    

class UniqueNameMixin:
    """Mixin to validate that the name field is unique."""
    def clean(self):
        if self.__class__.objects.filter(name=self.name).exclude(pk=self.pk).exists():
            raise ValidationError(f"{self.__class__.__name__} with this name already exists")
        super().clean()

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class CreatedByMixin:
    """Mixin to set the created_by field to the current user."""
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        """Ensure created_by is set to the current user."""
        user = self.context.get('request').user
        validated_data['created_by'] = user
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        """Ensure created_by is not updated."""
        validated_data.pop('created_by', None)  # Ensure created_by is not updated
        return super().update(instance, validated_data)
    
    class Meta:
        abstract = True
