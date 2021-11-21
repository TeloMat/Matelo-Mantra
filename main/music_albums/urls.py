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
    path("<int:id>/credits/create/", views.create_credit, name="create_credit"),
    path("credits/<int:id>/delete/", views.delete_credit, name="delete_credit"),

    path("Albums/list/", views.malbum_list, name="restMalbumsList"),
    path("Albums/<int:id>/", views.malbum, name="restSingleMalbum"),
    path("Albums/songs/album=<int:id>/", views.song_list, name="restSongList"),
    path("Albums/songs/<int:id>/", views.song, name="restSong"),

]

