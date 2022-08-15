from rest_framework import serializers
from .models import Post, Review
from users.serializers import *

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('post', )



class PostSerializer(serializers.ModelSerializer):
    writer = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:

        model = Post

        fields = (
            'title',
            'writer',
            'content',
            'created_at',
            'updated_at',
            'sub_content',
            'like_users',
            'view_users',
            'tag',
            'reviews'
        )
        