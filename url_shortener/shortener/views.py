from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ShortURL
from .serializers import ShortURLSerializer, URLCreateSerializer, URLUpdateSerializer
from django.shortcuts import redirect, render  
from django.conf import settings


def index(request):
    return render(request, 'index.html')

class ShortenURLView(APIView):
    def post(self, request):
        serializer = URLCreateSerializer(data=request.data)
        if serializer.is_valid():
            short_url = ShortURL.objects.create(url=serializer.validated_data['url'])
            return Response(ShortURLSerializer(short_url).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class URLDetailView(APIView):
    def get_object(self, short_code):
        try:
            return ShortURL.objects.get(short_code=short_code)
        except ShortURL.DoesNotExist:
            return None

    def get(self, request, short_code):
        short_url = self.get_object(short_code)
        if not short_url:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        short_url.access_count += 1
        short_url.save()
        
        if request.accepted_renderer.format == 'html':
            return redirect(short_url.url)
        return Response(ShortURLSerializer(short_url).data)

    def post(self, request, short_code):
        short_url = self.get_object(short_code)
        if not short_url:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if 'update' in request.path:
            serializer = URLUpdateSerializer(data=request.data)
            if serializer.is_valid():
                short_url.url = serializer.validated_data['url']
                short_url.save()
                return Response(ShortURLSerializer(short_url).data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif 'delete' in request.path:
            short_url.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

class URLStatsView(APIView):
    def get(self, request, short_code):
        try:
            short_url = ShortURL.objects.get(short_code=short_code)
            return Response(ShortURLSerializer(short_url).data)
        except ShortURL.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)