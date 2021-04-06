from django.urls import path
from . import views
from .views import PostView, CreatePostView

urlpatterns = [

    path("<int:id>", views.index, name="Index"),
    path("home/", views.home, name="Home"),
    path("", views.landing, name="landing"),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view"),
    path("postview/", PostView.as_view()),
    path("Createview/", CreatePostView.as_view())

]