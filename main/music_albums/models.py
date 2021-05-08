from django.db import models


class MusicAlbum(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=True)
    cover = models.ImageField(upload_to='music/covers', blank=True)


class Song(models.Model):
    album = models.ForeignKey(MusicAlbum, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    track = models.FileField(upload_to='music/tracks')
