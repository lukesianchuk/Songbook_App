from django.urls import path
from . import views

urlpatterns = [
    path("", views.song_index, name="song_index"),
    path("<int:pk>/", views.song_detail, name="song_detail"),
]