from random import random

from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import redirect, render

from .forms import CreateNewAlbum, EditAlbum, AddAlbumPicture
from .models import PictureAlbum, Picture


# def indexAlbum(response, id):
#     if not response.user.is_authenticated:
#         return HttpResponseForbidden()
#     album = PictureAlbum.objects.get(id=id)
#     if response.method == "Post":
#         pass
#
#     # form = EditAlbum(album)
#
#    pass


def indexAlbum(response, id):
    if not response.user.is_authenticated:
        return HttpResponseForbidden()
    album = PictureAlbum.objects.get(id=id)
    # if redirecting from edit
    if response.method == "POST":
        form = EditAlbum(album, response.POST)
        if form.is_valid():
            album.title = form.cleaned_data["title"]
            album.text = form.cleaned_data["description"]
            album.public = form.cleaned_data["public"]
            album.save()
            if (response.FILES.get('thumbnail')):
                album.thumbnail.save(album.title + "_tb", response.FILES.get('thumbnail'))
                album.save()
            return HttpResponseRedirect("/api/travels/")

    form = EditAlbum(album)
    picForm = AddAlbumPicture()

    return render(response, "main/picture_albums/album.html",
                  {"album": album, "form": form, "picForm": picForm})

def listAlbum(response):
    if response.user.is_authenticated:
        albumList = PictureAlbum.objects.all()
        return render(response, "main/picture_albums/albumList.html", {"list": albumList})
    return HttpResponseForbidden()





def createAlbum(response):
    if not response.user.is_authenticated:
        return HttpResponseForbidden()
    if response.method == "POST":
        form = CreateNewAlbum(response.POST, response.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            album = PictureAlbum()
            album.title = cd.get('title')
            album.public = cd.get('public')
            album.description = cd.get('description')
            if (response.FILES.get('thumbnail')):
                album.thumbnail.save(album.title + "_tb", response.FILES.get('thumbnail'))
            album.save()
            return HttpResponseRedirect("/api/travels/")
    form = CreateNewAlbum()
    return render(response, "main/picture_albums/albumCreate.html", {"form": form})


def deleteAlbum(response, id):
    if not response.user.is_authenticated:
        return HttpResponseForbidden()
    album = PictureAlbum.objects.get(id=id)
    album.thumbnail.delete()
    album.delete()
    return redirect('/api/travels/')


def addAlbumImage(response, id):
    if not response.user.is_authenticated:
        return HttpResponseForbidden()
    form = AddAlbumPicture(response.POST, response.FILES)
    if not response.FILES.get('photo'):
        return HttpResponseForbidden()
    if form.is_valid():
        album = PictureAlbum.objects.get(id=id)
        cd = form.cleaned_data
        album.picture_set.create(caption=cd.get('caption'), photo=response.FILES.get('photo'))

    return HttpResponseRedirect("/api/travels/"+str(id))


def deleteAlbumImg(response, id):
    if not response.user.is_authenticated:
        return HttpResponseForbidden()
    picture = Picture.objects.get(id=id)
    picture.photo.delete()
    picture.delete()
    return redirect('/api/travels/'+str(id))