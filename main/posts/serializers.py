from rest_framework import serializers

from main.posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'name', 'text', 'public', 'created_at')

# class PostCreditSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ('id', 'name', 'text', 'public', 'created_at')
#




class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('name',)
