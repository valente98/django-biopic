from django.shortcuts import render
from PIL import Image
from app import models


# Create your views here.
def imageInput(request):
    imageInputModel = models.ImageUploadModel(request.GET)
    return render(request, 'app/feed.html', {
        'form': imageInputModel,
    })