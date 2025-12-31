from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from index.models import Banner, Quotes
from .serializers import BannerSerializer, QuotesSerializer

class BannerListAPIView(APIView):
    def get(self, request):
        banner = Banner.objects.filter(is_active=True)
        serializer = BannerSerializer(banner, many=True, context={'request': request})
        return Response(serializer.data)

class QuotesListAPIView(APIView):
    def get(self, request):
        quotes = Quotes.objects.filter(is_featured=True)
        serializer = QuotesSerializer(quotes, many=True)
        return Response(serializer.data,)
    
