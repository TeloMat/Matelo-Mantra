from django.urls import path
from . import views
#from .views import PostView, CreatePostView

urlpatterns = [



    path("", views.listPost, name="listPost"),
    path("<int:id>", views.indexPost, name="indexPost"),
    path("create/", views.createPost, name="createPost"),











  #  path("postview/", PostView.as_view()),
   # path("Createview/", CreatePostView.as_view())

]