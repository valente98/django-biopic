from django import forms
from PIL import Image
from app.models import ImagePostModel


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImagePostModel
        fields = ('uploaded_by', 'image', 'caption')