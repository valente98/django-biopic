from django import forms
from PIL import Image
from app.models import ImagePostModel


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImagePostModel
        fields = ('caption', 'image', 'uploaded_by')