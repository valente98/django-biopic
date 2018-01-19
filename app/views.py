from django.shortcuts import render, redirect
from PIL import Image, ImageFilter
from django.views import View
from app.forms import *
from app.models import ImagePostModel
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

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
        objects = ImagePostModel.objects.all().order_by('-uploaded_at')
        return render(request, 'app/base.html',
                      {'objects': objects,
                       'c_form': CommentForm()})


class DeleteImage(View):
    def post(self, request, img_id):
        ImagePostModel.objects.get(id=img_id).delete()
        return redirect('app:base')


class FiltersChoice(View):
    def get(self, request, img_id):
        form = Filters()
        return render(request, 'app/filter.html', {'form': form})

    def post(self, request, img_id):
        form = Filters(request.POST)
        path = 'app/static/' + ImagePostModel.objects.get(
            id=img_id).image_url()
        image = Image.open(path)
        if form.is_valid():
            filter_choice = form.filters()
            image.convert('RGB').filter(filter_choice).save(path)
            return redirect("app:base")
        else:
            return render(request, 'app/filter.html', {'form', form})


class Likes(View):
    def post(self, request, img_id):
        count = ImagePostModel.objects.get(id=img_id)
        count.likes += 1
        count.save()
        return redirect('app:base')


class Comments(View):
    def post(self, request, img_id):
        document = ImagePostModel.objects.get(id=img_id)
        form = CommentForm(document, request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:base')
        else:
            return redirect('app:base')


class MostLikes(View):
    def get(self, request):
        objects = ImagePostModel.objects.all().order_by('-likes')[:4]
        return render(request, 'app/most_like.html', {'objects': objects})


class Mostcomments(View):
    def get(self, request):
        objects = ImagePostModel.objects.all().order_by('-comments')[:3]
        return render(request, 'app/most_comments.html',
                      {'objects': objects,
                       'c_form': CommentForm()})


class Signup(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'app/signup.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.refresh_from_db(
                )  # load the profile instance created by the signal
                user.profile.birth_date = form.cleaned_data.get('birth_date')
                user.save()
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(
                    username=user.username, password=raw_password)
                login(request, user)
                return redirect('app:base')
        else:
            form = SignUpForm()
        return render(request, 'app/signup.html', {'form': form})
