from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView

from .models  import Post, Item
from .forms import CreateNewPost
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



def index(response, id):
    if not response.user.is_authenticated:
        return HttpResponseForbidden()
    post = Post.objects.get(id=id)
    # if redirecting from edit
    if response.method == "POST":
        if response.POST.get("save"):
            for item in post.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.private = True
                else:
                    item.private = False
                item.save()
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")
            if len(txt) > 2:
                post.item_set.create(description=txt, private=False)
            else:
                print("invalid input")

        return render(response, "main/post.html", {"post": post})
    return render(response, "main/view.html", {})


def editPost(response, id):
    pass

def listPost(response):
    if response.user.is_authenticated:
        pList = Post.objects.filter()

        return render(response, "main/postList.html", {"list": pList})
    return HttpResponseForbidden()

def home(response):
    return render(response, "main/home.html", {})




def createPost(response):
    if response.method == "POST":
        form = CreateNewPost(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = form.cleaned_data["text"]
            pub = form.cleaned_data["public"]
            p = Post(name=n, text=t, public=pub)
            p.save()
            return HttpResponseRedirect("/api/%i" %p.id)
    else:
        form = CreateNewPost()
    return render(response, "main/postCreate.html", {"form":form})


def view(response):
    return render(response, "main/view.html")

