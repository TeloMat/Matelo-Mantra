from rest_framework import serializers

from main.music_albums.models import MusicAlbum, Song, AlbumCredit


class SongPlayerSerializer(serializers.ModelSerializer):
    track = serializers.FileField()
    album = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Song
        fields = ('title', 'album', 'artists', 'track', 'track_duration')


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'title', 'artists', 'description', 'track_duration')


class credit_serializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumCredit
        fields = ('contributor', 'contribution')


class MAlbumSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)
    credits = credit_serializer(many=True, read_only=True)
    cover = serializers.ImageField()

    class Meta:
        model = MusicAlbum
        fields = ('id', 'title', 'artist', 'description', 'cover', 'songs', 'credits')

