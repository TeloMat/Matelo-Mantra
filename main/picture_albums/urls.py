from django.urls import path
from . import views
#from .views import PostView, CreatePostView

urlpatterns = [
    path("", views.listPAlbum, name="listPAlbum"),
    path("create/", views.createPAlbum, name="createPAlbum"),
    path("<int:id>/", views.indexPAlbum, name="indexPAlbum"),
    path("<int:id>/delete", views.deletePAlbum, name="deletePAlbum"),
    path("<int:id>/addImage", views.addPAlbumImage, name="addPAlbumImage"),
    path("<int:id>/deleteImg", views.deletePAlbumImg, name="deletePAlbumImage"),
    path("<int:id>/addTag", views.addPAlbumTag, name="addPAlbumTag"),
    path("pic/<int:id>", views.displayPicture, name="displayPicture")

]