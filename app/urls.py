from django.urls import path, include
from app import views

app_name = 'app'

urlpatterns = [
    path('upload/', views.UploadImage.as_view(), name="upload"),
    path('base/', views.ShowImages.as_view(), name="base"),
    path('delete/<img_id>', views.DeleteImage.as_view(), name="delete")
]