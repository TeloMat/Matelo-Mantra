from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from .posts import urls as posts
from .picture_albums import urls as pAlbums
from .music_albums import urls as mAlbums

#from .views import PostView, CreatePostView
from .posts import urls
from .views import PostView

urlpatterns = [

    path("", views.landing, name="landing"),
    path("home/", views.home, name="Home"),
    path("post/", include(posts)),
    path("travels/", include(pAlbums)),
    path("music/", include(mAlbums)),
    path("test/", PostView().as_view())

]