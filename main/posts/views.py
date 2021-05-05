from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import redirect, render

from main.forms import EditPost, CreateNewPost
from .model import Post


def indexPost(response, id):
    if not response.user.is_authenticated:
        return HttpResponseForbidden()
    post = Post.objects.get(id=id)
    # if redirecting from edit
    if response.method == "POST":
        form = EditPost(post, response.POST)
        if form.is_valid():
            post.name = form.cleaned_data["name"]
            post.text = form.cleaned_data["text"]
            post.public = form.cleaned_data["public"]
            post.save()
            return redirect('/api/post')

    form = EditPost(post)

    return render(response, "main/posts/post.html", {"form": form})

def deletePost(response, id):
    if not response.user.is_authenticated:
        return HttpResponseForbidden()
    Post.objects.get(id=id).delete()
    return redirect('/api/post')


def listPost(response):
    if response.user.is_authenticated:
        pList = Post.objects.filter()

        return render(response, "main/posts/postList.html", {"list": pList})
    return HttpResponseForbidden()



def createPost(response):
    if response.method == "POST":
        form = CreateNewPost(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = form.cleaned_data["text"]
            pub = form.cleaned_data["public"]
            p = Post(name=n, text=t, public=pub)
            p.save()
            return HttpResponseRedirect("/api/post")
    else:
        form = CreateNewPost()
    return render(response, "main/posts/postCreate.html", {"form":form})



