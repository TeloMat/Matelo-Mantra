from django.contrib import admin
from .posts.models import Post
from .picture_album.models import PictureAlbum, Picture

# Register your models here.


admin.site.register(Post)
admin.site.register(PictureAlbum)
admin.site.register(Picture)
