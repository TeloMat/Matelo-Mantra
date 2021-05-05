from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .posts.views import *

from .forms import CreateNewPost, EditPost
from rest_framework import generics, status
# Create your views here.
from .serializers import PostSerializer, CreatePostSerializer


class PostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CreatePostView(APIView):
    serializer_class = CreatePostSerializer
    def post(self, request, format=None):
       # if not self.request.session.exists(self.request.session.session_key):
        #    pass
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.data.name
            p = Post(name=name)
            p.save()
        return Response(PostSerializer(p).data, status=status.HTTP_202)





def landing(response):
    return redirect("/api/home")



def home(response):
    return render(response, "main/home.html", {})

def view(response):
    return render(response, "main/view.html")

