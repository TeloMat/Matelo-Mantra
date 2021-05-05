from django.db import models


class PictureAlbum(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=True)

    def __str__(self):
        return "Title: " + self.title


class Picture(models.Model):
    album = models.ForeignKey(PictureAlbum, on_delete=models.CASCADE)
    caption = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='pAlbums/')