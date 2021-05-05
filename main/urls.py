from django.urls import path, include
from . import views, posts
from .posts import urls as posts
from .picture_album import urls as pAlbums

#from .views import PostView, CreatePostView
from .posts import urls

urlpatterns = [

    path("", views.landing, name="landing"),
    path("home/", views.home, name="Home"),
    path("post/", include(posts)),
    path("travels/", include(pAlbums))

]