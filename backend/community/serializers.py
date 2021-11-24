from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer): 
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username', 'mbti',)   

    class CommentSerializer(serializers.ModelSerializer):
        class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = get_user_model()
                fields = ('id', 'username', 'mbti',)   
        
        user = UserSerializer(read_only=True)    
        class Meta:
            model = Comment
            fields = ('id', 'content', 'updated_at', 'user')

    user = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = ('id', 'title', 'movie_title', 'created_at', 
        'updated_at', 'content', 'mbti', 'user_id', 'user','like_user', 'comments')

class ArticleSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Article
        fields = ('id', 'title', 'movie_title', 'created_at', 
        'updated_at', 'content', 'mbti', 'user_id')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'article_id', 'user_id', 'created_at','updated_at')


'''
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_article_comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)'''