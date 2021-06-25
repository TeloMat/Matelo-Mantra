from django.db import models
from django.contrib.auth.models import User



class Description(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField(max_length=800, blank=True)
    picture = models.ImageField(upload_to='descriptions/', blank=False)
    quote = models.CharField(max_length=200)
    public = models.BooleanField(default=False)
