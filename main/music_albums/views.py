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
        success = MusicAlbum().create_album()
        if success:
            return HttpResponseRedirect("/api/music/")
        return HttpResponseRedirect("/api/home/")
    form = CreateNewMAlbum()

    return render(response, "main/music_albums/albumCreate.html", {"form": form})


def indexMAlbum(response, id):
    if not response.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    album = MusicAlbum.objects.get(id=id)
    if response.method == "POST":
        success = album.edit_album(response)
        if not success:
            return HttpResponseRedirect("/api/home/")
        return HttpResponseRedirect("/api/music/")
    form = EditMAlbum(album)
    song_form = AddNewSong()
    credit_form = AddNewCredit()
    return render(response, "main/music_albums/album.html", {"album": album,
                                                             "form": form, "songForm": song_form,
                                                             "creditForm": credit_form})


def deleteMAlbum(response, id):
    if not response.user.is_authenticated:
        return HttpResponseRedirect('/login/')

    album = MusicAlbum.objects.get(id=id)
    album.delete_album()
    return HttpResponseRedirect("/api/music/")


def createSong(response, id):
    if not response.user.is_authenticated:
        return HttpResponseRedirect('/login/')

    success = MusicAlbum.objects.get(id=id).add_song(response)
    if success:
        return HttpResponseRedirect("/api/music/" + str(id) + "/")
    return HttpResponseRedirect("/api/home/")


def indexSong(response, id):
    if not response.user.is_authenticated:
        return HttpResponseRedirect('/login/')

    song = Song.objects.get(id=id)
    if response.method == "POST":
        success = song.edit_song(response)
        if success:
            return HttpResponseRedirect("/api/music/")
        return HttpResponseRedirect("/api/home/")

    form = EditSong(song)
    return render(response, "main/music_albums/albumSong.html",
                  {"song": song, "form": form})


def deleteSong(response, id):
    if not response.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    Song.objects.get(id=id).delete_song()
    return HttpResponseRedirect('/api/music/')


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
        songs = album.get_songs()
        if songs is not None:
            return JsonResponse()
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


def create_credit(request, id):
    if request.method == 'POST':
        success = MusicAlbum.objects.get(id).add_credit(request)
        if success:
            return HttpResponseRedirect("/api/travels/" + str(id) + "/")
        return HttpResponseRedirect("/api/home/")


def delete_credit(response, id):
    if not response.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    AlbumCredit.objects.get(id=id).delete_credit()
    return HttpResponseRedirect('/api/music/')
