from django.db import models
from PIL import Image


class OpenImageFile(models.Model):
    image = models.ImageField(upload_to="../app/static/app/photos")
