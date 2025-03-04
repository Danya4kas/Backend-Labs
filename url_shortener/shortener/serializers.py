from rest_framework import serializers
from .models import ShortURL

class ShortURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = ['id', 'url', 'short_code', 'created_at', 'updated_at', 'access_count']
        read_only_fields = ['id', 'short_code', 'created_at', 'updated_at', 'access_count']

class URLCreateSerializer(serializers.Serializer):
    url = serializers.URLField()

class URLUpdateSerializer(serializers.Serializer):
    url = serializers.URLField()