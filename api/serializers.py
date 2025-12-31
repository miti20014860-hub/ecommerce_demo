from rest_framework import serializers
from index.models import Banner, Quotes

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['id', 'image', 'caption', 'is_active']

class QuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotes
        fields = ['id', 'author', 'content', 'is_featured']