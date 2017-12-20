from django.shortcuts import render, redirect
from PIL import Image
from app import models, forms
from django.views import View
from app.forms import ImageUploadForm

# Create your views here.


class UploadImage(View):
    def get(self, request):
        form = ImageUploadForm()
        return render(request, 'app/feed.html', {
            'Image': form.Meta.model.image,
            'caption': form.Meta.model.caption
        })

    def post(self, request):
        form = ImageUploadForm()
        if form.is_valid():
            form.save()
            return redirect('app:feed')
        else:
            return render(request, 'app/upload.html', {'form': form})
