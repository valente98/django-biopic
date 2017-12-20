from django.db import models
from PIL import Image


class ImagePostModel(models.Model):
    caption = models.CharField(max_length=200)
    image = models.ImageField(upload_to="app/static/app/photos/")
