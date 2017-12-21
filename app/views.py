from django.shortcuts import render, redirect
from PIL import Image
from app import models, forms
from django.views import View
from app.forms import ImageUploadForm
from app.models import ImagePostModel

# Create your views here.


class UploadImage(View):
    def get(self, request):
        form = ImageUploadForm()
        return render(request, 'app/upload.html', {'form': form})

    def post(self, request):
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            caption = form.cleaned_data['caption']
            image = form.cleaned_data['image']
            uploaded_by = form.cleaned_data['uploaded_by']
            ImagePostModel(
                caption=caption, image=image, uploaded_by=uploaded_by).save()
            return redirect("app:base")
        else:
            return render(request, 'app/upload.html', {'form': form})


class ShowImages(View):
    def get(self, request):
        objects = ImagePostModel.objects.all()
        return render(request, 'app/base.html', {'objects': objects})


class DeleteImage(View):
    def post(self, request, img_id):
        ImagePostModel.objects.get(id=img_id).delete()
        return redirect('app:base')
