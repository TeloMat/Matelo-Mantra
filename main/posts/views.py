from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import redirect, render

from .forms import EditPost, CreateNewPost, AddPostCredit, AddPostTag
from .models import Post


def indexPost(response, id):
    if not response.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    post = Post.objects.get(id=id)
    # if redirecting from edit
    if response.method == "POST":
        form = EditPost(post, response.POST)
        if form.is_valid():
            post.name = form.cleaned_data["name"]
            post.text = form.cleaned_data["text"]
            post.public = form.cleaned_data["public"]
            post.save()
            return redirect('/api/post/')

    form = EditPost(post)
    tagForm = AddPostTag()
    creditForm = AddPostCredit()

    return render(response, "main/posts/post.html",
                  {"post": post, "form": form,
                   "tagForm": tagForm, "creditForm": creditForm})

def deletePost(response, id):
    if not response.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    Post.objects.get(id=id).delete()
    return redirect('/api/post/')

def listPost(response):
    if response.user.is_authenticated:
        pList = Post.objects.all()

        return render(response, "main/posts/postList.html", {"list": pList})
    return HttpResponseRedirect('/login/')


def createPost(response):
    if not response.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    if response.method == "POST":
        form = CreateNewPost(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = form.cleaned_data["text"]
            pub = form.cleaned_data["public"]
            p = Post(name=n, text=t, public=pub)
            p.save()
            return HttpResponseRedirect("/api/post/")
    form = CreateNewPost()
    return render(response, "main/posts/postCreate.html", {"form":form})


def addPostTag(response, id):
    if not response.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    form = AddPostTag(response.POST)
    if form.is_valid():
        post = Post.objects.get(id=id)
        tag_val = form.cleaned_data["val"]
        post.posttag_set.create(val=tag_val)

    return HttpResponseRedirect("/api/post/"+str(id))

def addPostCredit(response, id):
    if not response.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    form = AddPostCredit(response.POST)
    if form.is_valid():
        post = Post.objects.get(id=id)
        contributor = form.cleaned_data["contributor"]
        contribution = form.cleaned_data["contribution"]
        post.postcredit_set.create(contributor=contributor, contribution=contribution)
    return HttpResponseRedirect("/api/post/"+str(id))
