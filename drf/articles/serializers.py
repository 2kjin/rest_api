from rest_framework import serializers
from .models import Article, Comment

class ArticleListserializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)

class ArticleTitleserializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('title',)

class Commentserializer(serializers.ModelSerializer):
    article = ArticleTitleserializer(read_only=True)

    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ('id',)
        read_only_fields = ('article',)

class Articleserializer(serializers.ModelSerializer):
    comments = Commentserializer(many=True, read_only=True)
    commnet_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'