from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models  import Post, Item
from .forms import CreateNewPost
from rest_framework import generics
# Create your views here.
from .serializers import PostSerializer


class PostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



def landing(response):
    return redirect("/home")



def index(response, id):
    post = Post.objects.get(id=id)
    if post in response.user.post_set.all():

        if response.method== "POST":
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

        return render(response, "main/post.html", { "post" : post})
    return render(response, "main/view.html", {})


def home(response):
    return render(response, "main/home.html", {})


def create(response):
#    response.user
    if response.method == "POST":
        form = CreateNewPost(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            p = Post(name=n)
            p.save()
            response.user.post_set.add(p)

        return HttpResponseRedirect("/%i" %p.id)
    else:
        form = CreateNewPost()
    return render(response, "main/create.html", {"form":form})


def view(response):
    return render(response, "main/view.html")

