from django.urls import path
from . import views
#from .views import PostView, CreatePostView

urlpatterns = [
    path("", views.listAlbum, name="listAlbum"),
    path("create/", views.createAlbum, name="createAlbum"),
    path("<int:id>", views.indexAlbum, name="indexAlbum"),
    path("<int:id>/delete", views.deleteAlbum, name="deleteAlbum"),

]