from rest_framework import serializers

from main.posts.models import Post, PostCredit


class CreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCredit
        fields = ('id', 'contributor', 'contribution')


class PostSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField()
    credits = CreditSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'name', 'text', 'thumbnail', 'credits')

