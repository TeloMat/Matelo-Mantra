from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import redirect, render

from .forms import *
from .models import *


def listMAlbum(response):
    if not response.user.is_authenticated:
        return HttpResponseForbidden()
    albumList = MusicAlbum.objects.all()
    return render(response, "main/music_albums/albumList.html", {"list": albumList})


def createMAlbum(response):
    if not response.user.is_authenticated:
        return HttpResponseForbidden()
    if response.method == "POST":
        form = CreateNewMAlbum(response.POST, response.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            album = MusicAlbum()
            album.title = cd.get('title')
            album.artist = cd.get('artist')
            album.description = cd.get('description')
            album.public = cd.get('public')
            if response.FILES.get('cover'):
                album.cover.save(album.title + "_cover.jpg", response.FILES.get('cover'))
            album.save()
            return HttpResponseRedirect("/api/music/")

    form = CreateNewMAlbum()

    return render(response, "main/music_albums/albumCreate.html", {"form": form})


def indexMAlbum(response, id):
    if not response.user.is_authenticated:
        return HttpResponseForbidden()
    album = MusicAlbum.objects.get(id=id)

    if response.method == "POST":
        form = EditMAlbum(album, response.POST)
        if form.is_valid():
            cd = form.cleaned_data
            album.title = cd.get('title')
            album.artist = cd.get('artist')
            album.description = cd.get('description')
            album.public = cd.get('public')
            if response.FILES.get('cover'):
                album.cover.save(album.title + "cover",
                                 response.FILES.get('cover'))
            album.save()
            return HttpResponseRedirect("/api/music/")

    form = EditMAlbum(album)
    return render(response, "main/music_albums/album.html", {"album": album,
                                                             "form": form})


def deleteMAlbum(response, id):
    if not response.user.is_authenticated:
        return HttpResponseForbidden()
    album = MusicAlbum.objects.get(id=id)
    album.cover.delete()
    album.delete()
    return HttpResponseRedirect("/api/music/")


def createSong(response, id):
    if not response.user.is_authenticated:
        return HttpResponseForbidden()

    form = AddNewSong(response.POST, response.FILES)
    if not response.FILES('track'):
        return HttpResponseForbidden()
    if form.is_valid():
        album = MusicAlbum.objects.get(id=id)
        cd = form.cleaned_data
        album.song_set.create(
            title=cd.get('title'),
            description=cd.get('description'),
            track=response.FILES.get('track')
        )

    return HttpResponseRedirect("/api/music/" + str(id))


def indexSong(response, id):
    if not response.user.is_authenticated:
        return HttpResponseForbidden()
    return None


def deleteSong(response, id):
    if not response.user.is_authenticated:
        return HttpResponseForbidden()
    return None