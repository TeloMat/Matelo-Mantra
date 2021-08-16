from rest_framework import serializers

from main.picture_albums.models import PictureAlbum, Picture


class PAlbumSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField()

    class Meta:
        model = PictureAlbum
        fields = ('id', 'title', 'description', 'thumbnail')


class PictureSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField()

    class Meta:
        model = Picture
        fields = ('id', 'caption', 'photo')


class PAlbumDetailsSerializer(serializers.ModelSerializer):
    pictures = PictureSerializer(many=True, read_only=True)
    thumbnail = serializers.ImageField()

    class Meta:
        model = PictureAlbum
        fields = ('id', 'title', 'description', 'thumbnail', 'pictures')
