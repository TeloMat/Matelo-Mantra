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
    songForm = AddNewSong()
    return render(response, "main/music_albums/album.html", {"album": album,
                                                             "form": form, "songForm": songForm})


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
    if not response.FILES.get('track'):
        return HttpResponseForbidden()
    if form.is_valid():
        album = MusicAlbum.objects.get(id=id)
        cd = form.cleaned_data
        album.song_set.create(
            title=cd.get('title'),
            description=cd.get('description'),
            track=response.FILES.get('track')
        )

    return HttpResponseRedirect("/api/music/" + str(id) + "/")


def indexSong(response, id):
    if not response.user.is_authenticated:
        return HttpResponseForbidden()
    song = Song.objects.get(id=id)
    if response.method == "POST":
        form = EditSong(Song, response.POST, response.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            album = MusicAlbum.objects.filter(id=song.album_id)
            song.title = cd.get('title')
            if cd.get('description'):
                song.description = cd.get('description')
            if cd.get('track'):
                song.track = cd.get('track')
            song.save()
            return HttpResponseRedirect("/api/music/" + str(song.album_id) + "/")
    form = EditSong(song)
    return render(response, "main/music_albums/albumSong.html",
                  {"song": song, "form": form})


def deleteSong(response, id):
    if not response.user.is_authenticated:
        return HttpResponseForbidden()
    song = Song.objects.get(id=id)
    album_id = song.album_id
    song.track.delete()
    song.delete()
    return HttpResponseRedirect('/api/music/' + str(album_id) + '/')
