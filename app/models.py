from django.db import models
from PIL import Image


class ImageUploadModel(models.Model):
    # upload = models.FileField(upload_to='static/app/photos')
    message = Image.open('app/phot')
    # image = models.ImageField(upload_to='app/photos/')
