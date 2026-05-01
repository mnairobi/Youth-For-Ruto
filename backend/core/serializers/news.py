from rest_framework import serializers
from core.models import NewsCategory, NewsArticle


class NewsCategorySerializer(serializers.ModelSerializer):

    article_count = serializers.IntegerField(
        source='articles.count',
        read_only=True,
    )

    class Meta:
        model  = NewsCategory
        fields = '__all__'


class NewsListSerializer(serializers.ModelSerializer):
    """Lightweight serializer used for list / card views."""

    category_name = serializers.CharField(
        source='category.name',
        read_only=True,
        default='',
    )

    class Meta:
        model  = NewsArticle
        fields = [
            'id',
            'title',
            'slug',
            'category',
            'category_name',
            'excerpt',
            'featured_image',
            'author',
            'is_featured',
            'views',
            'created_at',
        ]


class NewsDetailSerializer(serializers.ModelSerializer):
    """Full serializer used for the single-article detail view."""

    category_name = serializers.CharField(
        source='category.name',
        read_only=True,
        default='',
    )

    class Meta:
        model  = NewsArticle
        fields = '__all__'