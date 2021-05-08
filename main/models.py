from django.db import models
from django.contrib.auth.models import User
from .posts import models
from .picture_albums import models
from .music_albums import models





# class Item(models.Model):
#      post = models.ForeignKey(Post, on_delete= models.CASCADE)
#      description = models.CharField(max_length=500)
#      private = models.BooleanField()
#
#      def __str__(self):
#          return self.description
# #
