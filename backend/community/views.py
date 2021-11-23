from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .serializers import ArticleSerializer
from . models import Article
# Create your views here.


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def article_list_create(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        # serializer = TodoSerializer(request.user.todos, many=True) # todos.all()이랑 같이 작동함..
        return Response(serializer.data)
    else:
        # print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
        # 왜 POST일 때 인증 안된 것을 막아주는지 모르겠음. 위에 ㅋㅋㅋㅋ가 프린트 안됨
        # Front에서 로그인 안한 경우 JWT 토큰을 헤더에 안담는데, 이게 POST일때는 꼭 JWT 토큰이 필요한가? 여기까지 일단 고민.
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([AllowAny])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def article_update_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if not request.user.articles.filter(pk=article_pk).exists():
        return Response({'error': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            # print(serializer)
            # serializer.user = request.user
            serializer.save()
            return Response(serializer.data)
    else:
        article.delete()
        return Response({ 'id': article_pk })