from rest_framework.response import Response
from rest_framework.views import APIView
from .posts.views import *
from .picture_albums.views import *

from rest_framework import generics, status
# Create your views here.


def landing(response):
    return redirect("/api/home/")


def home(response):
    return render(response, "main/home.html", {})


def view(response):
    return render(response, "main/view.html")
