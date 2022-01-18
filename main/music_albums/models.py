from operator import mod
from django.db import models
from mutagen import mp3

from main.music_albums.forms import CreateNewMAlbum, AddNewSong, EditMAlbum, EditSong, AddNewCredit


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
            cleaned_data = form.cleaned_data
            self.handle_data(cleaned_data)
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
        for song in self.songs.all():
            song.delete_song()
        for credit in self.credits.all():
            credit.delete()
        self.delete()

    def add_song(self, response):
        form = AddNewSong(response.POST, response.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            self.songs.create(
                title=cleaned_data.get('title'),
                description=cleaned_data.get('description'),
                artists=cleaned_data.get('artists'),
                track=response.FILES.get('track'),
                track_duration=mp3.MP3(response.FILES.get('track')).info.length
            )
            return True
        return False

    def get_songs(self):
        if not self.public:
            return None
        return Song.objects.filter(self.id)

    def add_credit(self, response):
        form = AddNewCredit(response.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            self.credits.create(
                contributor=cleaned_data.get('contributor'),
                contribution=cleaned_data.get('contribution'),
            )
            return True
        return False


class AlbumCredit(models.Model):
    album = models.ForeignKey(MusicAlbum, related_name='credits', on_delete=models.CASCADE)
    contributor = models.CharField(max_length=50)
    contribution = models.CharField(max_length=200, blank=True)

    def delete_credit(self):
        self.delete()

def validate_file_extension(value):
    if not value.name.endswith('.mp3'):
        raise ValidationError(u'Only mp3 files are supported!')


class Song(models.Model):
    album = models.ForeignKey(MusicAlbum, related_name='songs', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    artists = models.CharField(max_length=100, default="Matelo Mantra")
    description = models.CharField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    track = models.FileField(upload_to='music/tracks', validators=[validate_file_extension])
    track_duration = models.FloatField(default=0)

    def delete_song(self):
        self.track.delete()
        self.delete()

    def edit_song(self, response):
        form = EditSong(self, response.POST, response.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data

            self.title = cleaned_data.get("title")
            self.artists = cleaned_data.get("artists")
            if cleaned_data.get("description"):
                self.description = cleaned_data.get("description")
            if cleaned_data.get("track"):
                self.track.save(self.title + "_track.mp3", cleaned_data.get('track'))
            self.save()
            return True
        return False

