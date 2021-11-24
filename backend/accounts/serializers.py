from rest_framework import serializers
from django.contrib.auth import get_user_model

from community.models import Article
class UserSerializer(serializers.ModelSerializer):

    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('id', 'title', 'movie_title', 'created_at', 
            'updated_at', 'content', 'mbti', 'user_id', 'user','like_user', 'comments')
    
    articles = ArticleSerializer(many=True, read_only=True)
    password = serializers.CharField(write_only=True)
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password', 'mbti', 'email', 'articles',)