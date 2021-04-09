from django.urls import path
from . import views
from .views import PostView, CreatePostView

urlpatterns = [

    path("", views.landing, name="landing"),
    path("home/", views.home, name="Home"),
    path("post/", views.listPost, name="listPost"),
    path("post/<int:id>", views.index, name="IndexPost"),
    path("post/create/", views.createPost, name="createPost"),
    path("post/edit/<int:id>", views.editPost, name="editPost"),
    path("view/", views.view, name="view"),
    path("postview/", PostView.as_view()),
    path("Createview/", CreatePostView.as_view())

]