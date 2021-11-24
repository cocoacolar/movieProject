from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Genre, Movie, Comment

class MovieSerializer(serializers.ModelSerializer):

    class CommentSerializer(serializers.ModelSerializer):
        class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = get_user_model()
                fields = ('id', 'username', 'mbti',)   

        user = UserSerializer(read_only=True)    
        class Meta:
            model = Comment
            fields = ('id', 'content', 'updated_at', 'rank', 'user')

    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ('id', 'title', 'release_date', 'vote_count', 
        'popularity', 'vote_average', 'overview', 'poster_path', 'genres', 'comments',)

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name',)

class CommentSerializer(serializers.ModelSerializer):     
    class Meta:
        model = Comment
        fields = ('id', 'content', 'movie_id', 'user_id', 'created_at','updated_at', 'rank')
