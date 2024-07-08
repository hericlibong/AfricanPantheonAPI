from django import forms
from django.core.exceptions import ValidationError

  
class UniqueNameAdminForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data['name']
        if self._meta.model.objects.filter(name=name).exists():
            raise ValidationError(f"{self._meta.model.__name__} with this name already exists")
        return name
