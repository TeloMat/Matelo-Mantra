from django.contrib import admin

from .music_albums.models import *
from .posts.models import *
from .picture_albums.models import *

# Register your models here.


admin.site.register(Post)
admin.site.register(PostTag)
admin.site.register(PostCredit)
admin.site.register(PictureAlbum)
admin.site.register(Picture)
admin.site.register(PictureTag)
admin.site.register(MusicAlbum)
admin.site.register(Song)

