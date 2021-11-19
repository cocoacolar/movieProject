from rest_framework import serializers
from .models import Article, Comment

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'movie_title', 'created_at', 'updated_at', 'content', 'mbti',)

'''
    title = models.CharField(max_length=100)
    movie_title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    like = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_articles')
    mbti = models.CharField(blank=True, choices=MBTI_CHOICES, max_length=4) 
'''