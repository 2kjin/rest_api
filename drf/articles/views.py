from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from django.shortcuts import get_list_or_404, get_object_or_404

from .models import Article, Comment
from .serializers import ArticleListserializer, Articleserializer, Commentserializer


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListserializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Articleserializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = Articleserializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        res = { f' {article_pk}번째 글이 지워졌어욤!'}
        return Response(res, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = Articleserializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        comments = get_list_or_404(Comment)
        serializer = Commentserializer(comments, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = Commentserializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        res = { f' {comment_pk}번째 댓글이 지워졌어욤!'}
        return Response(res, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = Commentserializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['POST'])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = Commentserializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)