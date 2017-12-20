from django.urls import path, include
from app import views

app_name = 'app'

urlpatterns = [
    path('upload/', views.UploadImage.as_view(), name="upload"),
    path('feed/', views.UploadImage.as_view(), name="feed")
]