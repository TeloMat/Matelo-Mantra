from django.db import models
from django.contrib.auth.models import User


class Description(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField(max_length=800, blank=True)
    quote = models.CharField(max_length=300)
    picture = models.ImageField(upload_to='descriptions/profile', blank=False)
    musician = models.ImageField(upload_to='descriptions/musician')
    writer = models.ImageField(upload_to='descriptions/writer')
    traveler = models.ImageField(upload_to='descriptions/traveler')
    public = models.BooleanField(default=False)
