from rest_framework import viewsets
from index.models import Banner, News, Notice, Quote
from .serializers import BannerSerializer, NewsSerializer, NoticeSerializer, QuoteSerializer

class BannerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Banner.objects.filter(is_active=True)
    serializer_class = BannerSerializer

class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all().order_by('-created_at')
    serializer_class = NewsSerializer

class NoticeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Notice.objects.all().order_by('-created_at')
    serializer_class = NoticeSerializer

class QuoteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Quote.objects.filter(is_active=True)
    serializer_class = QuoteSerializer
