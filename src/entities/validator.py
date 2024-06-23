from PIL import Image
from django.core.exceptions import ValidationError

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
