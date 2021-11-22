import requests

from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .serializers import MovieSerializer
from . models import Movie

from pprint import pprint
# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    # serializer = TodoSerializer(request.user.todos, many=True) # todos.all()이랑 같이 작동함..
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def movie_detail(request, movie_pk):
    article = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(article)
    return Response(serializer.data)


# @api_view(['GET'])
# @permission_classes([AllowAny])
# def api_movie_list(request):
#     request_url = "https://api.themoviedb.org/3/movie/popular/?api_key=0cdf5d1b00a1a5e72e99fbb30ff4ec91&language=ko-KR&page=1"
#     data = requests.get(request_url).json()
#     movies = data.get('results')

#     pprint(movies)
#     print(type(movies[0]))

#     for movie in movies:
#         serializer = MovieSerializer(data=movie)
#         # print(serializer)   
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
    

#     return Response({'success': '데이터 로드 성공했습니다.'}, status=status.HTTP_200_OK)
