from django import forms
from PIL import Image


class OpenImageFile(forms.Form):
    Filepath = Image.open('../app/static/app/photos/ACE17FIFA.jpg')
