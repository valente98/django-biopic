from django.shortcuts import render
from PIL import Image
from app import forms

# Create your views here.


def imageInput(request):
    imageInputForm = forms.OpenImageFile(request.GET)
    return render(request, 'app/feed.html', {
        'form': imageInputModel,
    })