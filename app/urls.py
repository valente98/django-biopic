from django.urls import path, include
from app import views

app_name = 'app'

urlpatterns = [
    # path('login/', views.Login.as_view(), name="login"),
    # path('signup/', views.Signup.as_view(), name="signup")
    path('upload/', views.UploadImage.as_view(), name="upload"),
    path('base/', views.ShowImages.as_view(), name="base"),
    path('delete/<img_id>', views.DeleteImage.as_view(), name="delete"),
    path('filter/<img_id>', views.FiltersChoice.as_view(), name="filter"),
    path('choice/<img_id>', views.FiltersChoice.as_view(), name="choice"),
    path('likes/<img_id>', views.Likes.as_view(), name="likes"),
]