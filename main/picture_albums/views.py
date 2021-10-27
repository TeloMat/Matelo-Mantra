from random import random

from django.http import HttpResponseForbidden, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render

from .forms import *
from .models import *
from .serializers import PAlbumSerializer, PictureSerializer, PAlbumDetailsSerializer


def indexPAlbum(response, id):
    if not response.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    album = PictureAlbum.objects.get(id=id)
    # if redirecting from edit
    if response.method == "POST":
        success = album.edit_album(response)
        if success:
            return HttpResponseRedirect("/api/travels/")
        return HttpResponseRedirect("/api/home/")
    form = EditPAlbum(album)
    picForm = AddPAlbumPicture()
    tagForm = AddPAlbumTag()

    return render(response, "main/picture_albums/album.html",
                  {"album": album, "form": form, "picForm": picForm})


def listPAlbum(response):
    if response.user.is_authenticated:
        albumList = PictureAlbum.objects.all()
        return render(response, "main/picture_albums/albumList.html", {"list": albumList})
    return HttpResponseRedirect('/login/')


def createPAlbum(response):
    if not response.user.is_authenticated:
        return HttpResponseRedirect('/login/')

    if response.method == "POST":
        success = PictureAlbum().create_album(response)
        if success:
            return HttpResponseRedirect("/api/travels/")
        return HttpResponseRedirect("/api/home/")
    form = CreateNewPAlbum()
    return render(response, "main/picture_albums/albumCreate.html", {"form": form})


def deletePAlbum(response, id):
    if not response.user.is_authenticated:
        return HttpResponseRedirect('/login/')

    PictureAlbum.objects.get(id=id).delete_album()
    return HttpResponseRedirect('/api/travels/')


def addPAlbumImage(response, id):
    if not response.user.is_authenticated:
        return HttpResponseRedirect('/login/')

    form = AddPAlbumPicture(response.POST, response.FILES)
    if not response.FILES.get('photo'):
        return HttpResponseForbidden()
    album = PictureAlbum.objects.get(id=id)
    success = album.add_picture(response)
    if success:
        return HttpResponseRedirect("/api/travels/" + str(id) + "/")
    return HttpResponseRedirect("/api/home/")


def deletePAlbumImg(response, id):
    if not response.user.is_authenticated:
        return HttpResponseRedirect('/login/')

    Picture.objects.get(id=id).delete_picture()
    return redirect('/api/travels/' + str(id))


def addPAlbumTag(response, id):
    if not response.user.is_authenticated:
        return HttpResponseRedirect('/login/')

    form = AddPAlbumTag(response.POST)
    if form.is_valid():
        album = PictureAlbum.objects.get(id=id)
        tag_val = form.cleaned_data["val"]
        album.picturetag_set.create(val=tag_val)

    return HttpResponseRedirect("/api/travels/" + str(id) + '/')


def displayPicture(response, id):
    if not response.user.is_authenticated:
        return HttpResponseRedirect('/login/')

    picture = Picture.objects.get(id=id)
    url = picture.photo.url
    return HttpResponseRedirect(url)


def palbum_list(request):
    if request.method == 'GET':
        albums = PictureAlbum.objects.filter(public=True)
        serializer = PAlbumSerializer(albums, many=True)
        return JsonResponse(serializer.data, safe=False)
    # return JsonResponse()


def palbum(request, id):
    if request.method == 'GET':
        album = PictureAlbum.objects.get(public=True, id=id)
        serializer = PAlbumDetailsSerializer(album)
        return JsonResponse(serializer.data)
    # return JsonResponse()


def picture_list(request, id):
    if request.method == 'GET':
        album = PictureAlbum.objects.get(id=id)
        if not album.public:
            return JsonResponse()
        pictures = Picture.objects.filter(album_id=id)
        serializer = PictureSerializer(pictures, many=True)
        return JsonResponse(serializer.data, safe=False)
    # return JsonResponse()
