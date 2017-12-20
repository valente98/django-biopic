from django.db import models
from PIL import Image


class ImagePostModel(models.Model):
    caption = models.CharField(max_length=200)
    image = models.ImageField(upload_to="app/static/app/photos/")
    uploaded_by = models.CharField(max_length=20, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def image_url(self):
        return self.image.name[len('app/static/'):]