from django.db import models

from main.music_albums.forms import CreateNewMAlbum, AddNewSong, EditMAlbum


class MusicAlbum(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=True)
    cover = models.ImageField(upload_to='music/covers', blank=True)

    def __str__(self):
        return self.title

    def handle_files(self, cleaned_data):
        if cleaned_data.get('cover'):
            self.cover.save(self.title + "_cover.jpg", cleaned_data.get('cover'))

    def handle_data(self, cleaned_data):
        self.title = cleaned_data.get('title')
        self.artist = cleaned_data.get('artist')
        if cleaned_data.get('description'):
            self.description = cleaned_data.get('description')
        self.public = cleaned_data.get('public')
        self.handle_files(cleaned_data)
        self.save()

    def create_album(self, response, **kwargs):
        form = CreateNewMAlbum(response.POST, response.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            self.handle_data(cd)
            return True
        return False

    def edit_album(self, response, **kwargs):
        form = EditMAlbum(self, response.POST, response.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            self.handle_data(cd)
            return True
        return False

    def delete_album(self):
        self.cover.delete()
        for song in self.songs:
            song.track.delete()
            song.delete()
        for credit in self.credits:
            credit.delete()
        self.delete()

    def add_song(self, response):
        form = AddNewSong(response.POST, response.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            self.songs.create(
                title=cd.get('title'),
                description=cd.get('description'),
                artists=cd.get('artists'),
                track=response.FILES.get('track')
            )
            return True
        return False

    def get_songs(self):
        if not self.public:
            return None
        return Song.objects.filter(self.id)


class AlbumCredit(models.Model):
    album = models.ForeignKey(MusicAlbum, related_name='credits', on_delete=models.CASCADE)
    contributor = models.CharField(max_length=50)
    contribution = models.CharField(max_length=200, blank=True)


class Song(models.Model):
    album = models.ForeignKey(MusicAlbum, related_name='songs', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    artists = models.CharField(max_length=100, default="Matelo Mantra")
    description = models.CharField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    track = models.FileField(upload_to='music/tracks')

    def delete_song(self):
        self.track.delete()
        self.delete()




