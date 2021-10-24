from django.urls import path
from . import views

urlpatterns = [
    path("", views.listDesc, name="listDesc"),
    path("<int:id>/", views.indexDesc, name="indexDesc"),
    path("<int:id>/delete/", views.deleteDesc, name="deleteDesc"),
    path("create/", views.createDescription, name="createDescription"),
    path("rest/", views.get_curr_description, name="getRestDescription")
]