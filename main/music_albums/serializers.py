from rest_framework import serializers

from main.music_albums.models import MusicAlbum, Song


class SongPlayerSerializer(serializers.ModelSerializer):
    track = serializers.FileField()
    album = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Song
        fields = ('title', 'album', 'artists', 'description', 'track')

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('title', 'artists', 'description')


class MAlbumSerializer(serializers.ModelSerializer):
    songs = SongPlayerSerializer(many=True, read_only=True)
    cover = serializers.ImageField()
    class Meta:
        model = MusicAlbum
        fields = ('id', 'title', 'artist', 'description', 'cover',  'songs')

# class PostCreditSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ('id', 'name', 'text', 'public', 'created_at')
#


#
#
# class CreatMAlbumSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MusicAlbum
#
#         fields = ('name',)
