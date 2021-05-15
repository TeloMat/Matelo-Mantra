from django.urls import path
from . import views
#from .views import PostView, CreatePostView

urlpatterns = [

    path("", views.listPost, name="listPost"),
    path("<int:id>/", views.indexPost, name="indexPost"),
    path("<int:id>/delete/", views.deletePost, name="deletePost"),
    path("create/", views.createPost, name="createPost"),
    path("<int:id>/addTag/", views.addPostTag, name="addPostTag"),
    path("<int:id>/addCredit/", views.addPostCredit, name="addPostCredit")


#  path("postview/", PostView.as_view()),
# path("Createview/", CreatePostView.as_view())

]