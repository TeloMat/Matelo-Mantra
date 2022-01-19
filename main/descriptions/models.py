from django.db import models
from django.contrib.auth.models import User

from .forms import CreateNewDescription, EditDescription


class Description(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=350, blank=True)
    quote = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='descriptions/profile', blank=False)
    musician = models.ImageField(upload_to='descriptions/musician', blank=False)
    writer = models.ImageField(upload_to='descriptions/writer', blank=False)
    traveler = models.ImageField(upload_to='descriptions/traveler', blank=False)
    public = models.BooleanField(default=False)

    def handle_files(self, cleaned_data):
        if cleaned_data.get('picture'):
            self.picture.save(self.name + "_pp.jpg", cleaned_data.get('picture'))
        if cleaned_data.get('musician'):
            self.musician.save(self.name + "_menu1.jpg", cleaned_data.get('musician'))
        if cleaned_data.get('traveler'):
            self.traveler.save(self.name + "_menu2.jpg", cleaned_data.get('traveler'))
        if cleaned_data.get('writer'):
            self.writer.save(self.name + "_menu3.jpg", cleaned_data.get('writer'))

    def handle_data(self, cleaned_data):
        self.name = cleaned_data.get("name")
        if cleaned_data.get("text"):
            self.text = cleaned_data.get("text")
        self.quote = cleaned_data.get("quote")
        self.public = cleaned_data.get("public")
        if self.public:
            public_descriptions = Description.objects.filter(public=True)
            for desc in public_descriptions:
                desc.public = False
                desc.save()
        self.handle_files(cleaned_data)
        self.save()

    def create_description(self, response, **kwargs):
        form = CreateNewDescription(response.POST, response.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            self.handle_data(cd)
            return True
        return False

    def edit_description(self, response, **kwargs):
        form = EditDescription(self, response.POST, response.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            self.handle_data(cd)
            return True
        return False

    def delete_description(self):
        self.picture.delete()
        self.musician.delete()
        self.traveler.delete()
        self.writer.delete()
        self.delete()
