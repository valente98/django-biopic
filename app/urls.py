from django.urls import path, include
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.imageInput, name="home"),
]