from rest_framework import viewsets
from index.models import Banner, News, Quote
from .serializers import BannerSerializer, NewsSerializer,QuoteSerializer

class BannerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Banner.objects.filter(is_active=True)
    serializer_class = BannerSerializer

class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all().order_by('-created_at')
    serializer_class = NewsSerializer

class QuoteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Quote.objects.filter(is_active=True)
    serializer_class = QuoteSerializer
