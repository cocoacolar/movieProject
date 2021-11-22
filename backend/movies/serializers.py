from rest_framework import serializers
from .models import Movie, Comment

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'release_date', 'vote_count', 
        'popularity', 'vote_average', 'overview', 'poster_path')
