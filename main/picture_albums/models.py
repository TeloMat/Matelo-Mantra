from django.db import models


class PictureAlbum(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=True)
    thumbnail = models.ImageField(upload_to='travels/thumbnails', blank=True)

    def __str__(self):
        return "Title: " + self.title


class Picture(models.Model):
    album = models.ForeignKey(PictureAlbum, related_name='pictures', on_delete=models.CASCADE)
    caption = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='travels/pictures', blank=False)


class PictureTag(models.Model):
    album = models.ForeignKey(PictureAlbum, on_delete=models.CASCADE, null=True)
    val = models.CharField(max_length=15)

    def __str__(self):
        return self.val
