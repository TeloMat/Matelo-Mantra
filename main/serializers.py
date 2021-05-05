from rest_framework import  serializers
from .posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'name', 'created_at')




class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('name',)
