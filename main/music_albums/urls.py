from django.urls import path, include
from . import views


#from .views import PostView, CreatePostView

urlpatterns = [
    path("", views.listMAlbum, name="listMAlbum"),
    path("create/", views.createMAlbum, name="createMAlbum"),
    path("<int:id>/", views.indexMAlbum, name="indexMAlbum"),
    path("<int:id>/delete/", views.deleteMAlbum, name="listMAlbum"),
    path("<int:id>/createSong/", views.createSong, name="createSong"),
    path("songs/<int:id>/", views.indexSong, name="indexSong"),
    path("songs/<int:id>/delete/", views.deleteSong, name="deleteSong"),
    path("Albums/list/", views.malbum_list, name="restMalbumsList"),
    path("Albums/<int:id>/", views.malbum, name="restSingleMalbum"),
    path("Albums/songs/album=<int:id>/", views.song_list, name="restSongList"),
    path("Albums/songs/<int:id>/", views.song, name="restSong"),

]