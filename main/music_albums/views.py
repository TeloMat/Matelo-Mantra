from django.http import HttpResponseForbidden, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from rest_framework import generics

from .forms import *
from .models import *
from .serializers import MAlbumSerializer, SongSerializer, SongPlayerSerializer


def listMAlbum(response):
    if not response.user.is_authenticated:
        return HttpResponseRedirect('/login/')

    albumList = MusicAlbum.objects.all()
    return render(response, "main/music_albums/albumList.html", {"list": albumList})


def createMAlbum(response):
    if not response.user.is_authenticated:
        return HttpResponseRedirect('/login/')

    if response.method == "POST":
        form = CreateNewMAlbum(response.POST, response.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            album = MusicAlbum()
            album.title = cd.get('title')
            album.artist = cd.get('artist')
            if cd.get('description'):
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
        return HttpResponseRedirect('/login/')

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
                album.cover.save(album.title + "cover.jpg",
                                 response.FILES.get('cover'))
            album.save()
            return HttpResponseRedirect("/api/music/")

    form = EditMAlbum(album)
    songForm = AddNewSong()
    return render(response, "main/music_albums/album.html", {"album": album,
                                                             "form": form, "songForm": songForm})


def deleteMAlbum(response, id):
    if not response.user.is_authenticated:
        return HttpResponseRedirect('/login/')

    album = MusicAlbum.objects.get(id=id)
    album.cover.delete()
    album.delete()
    return HttpResponseRedirect("/api/music/")


def createSong(response, id):
    if not response.user.is_authenticated:
        return HttpResponseRedirect('/login/')

    form = AddNewSong(response.POST, response.FILES)
    if not response.FILES.get('track'):
        return HttpResponseForbidden()
    if form.is_valid():
        album = MusicAlbum.objects.get(id=id)
        cd = form.cleaned_data
        album.songs.create(
            title=cd.get('title'),
            description=cd.get('description'),
            artists=cd.get('artists'),
            track=response.FILES.get('track')
        )

    return HttpResponseRedirect("/api/music/" + str(id) + "/")


def indexSong(response, id):
    if not response.user.is_authenticated:
        return HttpResponseRedirect('/login/')

    song = Song.objects.get(id=id)
    if response.method == "POST":
        form = EditSong(Song, response.POST, response.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            song.title = cd.get('title')
            song.artists = cd.get('artists')
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
        return HttpResponseRedirect('/login/')

    song = Song.objects.get(id=id)
    album_id = song.album_id
    song.track.delete()
    song.delete()
    return HttpResponseRedirect('/api/music/' + str(album_id) + '/')


def malbum_list(request):
    if request.method == 'GET':
        albums = MusicAlbum.objects.filter(public=True)
        serializer = MAlbumSerializer(albums, many=True)
        return JsonResponse(serializer.data, safe=False)


def malbum(request, id):
    if request.method == 'GET':
        album = MusicAlbum.objects.get(public=True, id=id)
        serializer = MAlbumSerializer(album)
        return JsonResponse(serializer.data)
    # return JsonResponse()


def song_list(request, id):
    if request.method == 'GET':
        album = MusicAlbum.objects.get(id=id)
        if album.public != True:
            return JsonResponse()
        songs = Song.objects.filter(album_id=id)
        serializer = SongSerializer(songs, many=True)
        return JsonResponse(serializer.data, safe=False)
    # return JsonResponse()


def song(request, id):
    if request.method == 'GET':
        song = Song.objects.get(id=id)
        album = MusicAlbum.objects.get(id=song.album_id)
        if album.public == True:
            serializer = SongPlayerSerializer(song)
            return JsonResponse(serializer.data, safe=True)
    # return JsonResponse()
