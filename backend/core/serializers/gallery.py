from rest_framework import serializers
from core.models import GalleryCategory, GalleryImage


class GalleryCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model  = GalleryCategory
        fields = '__all__'


class GalleryImageSerializer(serializers.ModelSerializer):

    category_name = serializers.CharField(
        source='category.name',
        read_only=True,
        default='',
    )

    class Meta:
        model  = GalleryImage
        fields = '__all__'