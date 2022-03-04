from django import forms
from .models import ImageClassificationResult


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageClassificationResult
        fields = ("image",)
