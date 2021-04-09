from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField(max_length=800, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)

    def __str__(self):
        return "Title: " + self.name


class credit(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    contributor = models.CharField(max_length=50, )
    contribution = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.contributor + ": " + self.contribution

class tag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    val = models.CharField(max_length=15)

    def __str__(self):
        return self.val



class Item(models.Model):
     post = models.ForeignKey(Post, on_delete= models.CASCADE)
     description = models.CharField(max_length=500)
     private = models.BooleanField()

     def __str__(self):
         return self.description
#
