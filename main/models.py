from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name




class Item(models.Model):
     post = models.ForeignKey(Post, on_delete= models.CASCADE)
     description = models.CharField(max_length=500)
     private = models.BooleanField()

     def __str__(self):
         return self.description




# Create your models here.
