from django.db import models

from main.picture_albums.forms import CreateNewPAlbum, EditPAlbum, AddPAlbumPicture


class PictureAlbum(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=True)
    thumbnail = models.ImageField(upload_to='travels/thumbnails', blank=True)

    def __str__(self):
        return "Title: " + self.title

    def handle_files(self, cleaned_data):
        if cleaned_data.get('thumbnail'):
            self.thumbnail.save(self.title + "_thumbnail.jpg", cleaned_data.get('thumbnail'))

    def handle_data(self, cleaned_data):
        self.title = cleaned_data.get('title')
        self.artist = cleaned_data.get('artist')
        if cleaned_data.get('description'):
            self.description = cleaned_data.get('description')
        self.public = cleaned_data.get('public')
        self.handle_files(cleaned_data)
        self.save()

    def create_album(self, response, **kwargs):
        form = CreateNewPAlbum(response.POST, response.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            self.handle_data(cleaned_data)
            return True
        return False

    def edit_album(self, response, **kwargs):
        form = EditPAlbum(self, response.POST, response.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            self.handle_data(cd)
            return True
        return False

    def delete_album(self):
        self.thumbnail.delete()
        for picture in self.pictures:
            picture.delete_picture()
        self.delete()

    def add_picture(self, response):
        form = AddPAlbumPicture(response.POST, response.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            self.pictures.create(
                caption=cleaned_data.get('caption'),
                photo=response.FILES.get('photo')
            )
            return True
        return False

    def get_pictures(self):
        if not self.public:
            return None
        return Picture.objects.filter(self.id)


class Picture(models.Model):
    album = models.ForeignKey(PictureAlbum, related_name='pictures', on_delete=models.CASCADE)
    caption = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='travels/pictures', blank=False)

    def delete_picture(self):
        self.photo.delete()
        self.delete()
