from django.urls import path, include
from . import views


#from .views import PostView, CreatePostView

urlpatterns = [
    path("", views.listMAlbum, name="listMAlbum"),
    path("create/", views.createMAlbum, name="createMAlbum"),
    path("<int:id>/", views.indexMAlbum, name="indexMAlbum"),
    path("<int:id>/delete", views.deleteMAlbum, name="listMAlbum"),
    path("<int:id>/createSong/", views.createSong, name="createSong"),
    path("songs/<int:id>/", views.indexSong, name="indexSong"),
    path("songs/<int:id>/delete", views.deleteSong, name="deleteSong")

]