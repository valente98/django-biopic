from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class ImagePostModel(models.Model):
    caption = models.CharField(max_length=200)
    image = models.ImageField(upload_to="app/static/app/photos/")
    uploaded_by = models.CharField(max_length=20, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def image_url(self):
        return self.image.name[len('app/static/'):]


class Comments(models.Model):
    comment = models.CharField(max_length=180)
    time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(ImagePostModel, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()