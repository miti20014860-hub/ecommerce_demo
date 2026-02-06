from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from index.models import Banner, News, Notice, Quote
from activity.models import Activity, Booking
from .serializers import BannerSerializer, NewsSerializer, NoticeSerializer, QuoteSerializer, ActivitySerializer, BookingSerializer


# Index
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


# Activity
class ActivityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Activity.objects.all().order_by('-created_at')
    serializer_class = ActivitySerializer

    @action(detail=False, methods=['get'])
    def filters(self, request):
        def format_choices(choices):
            return [{'value': x[0], 'label': x[1]} for x in choices]

        return Response({
            'types': format_choices(Activity.Type_CHOICES),
            'appointment_options': format_choices(Activity.Appointment_CHOICES),
            'region_groups': [
                {'label': 'Hokkaido', 'prefectures': format_choices(
                    Activity.HOKKAIDO)},
                {'label': 'Tohoku', 'prefectures': format_choices(
                    Activity.TOHOKU)},
                {'label': 'Kanto', 'prefectures': format_choices(
                    Activity.KANTO)},
                {'label': 'Chubu', 'prefectures': format_choices(
                    Activity.CHUBU)},
                {'label': 'Kansai', 'prefectures': format_choices(
                    Activity.KANSAI)},
                {'label': 'Chugoku', 'prefectures': format_choices(
                    Activity.CHUGOKU)},
                {'label': 'Shikoku', 'prefectures': format_choices(
                    Activity.SHIKOKU)},
                {'label': 'Kyushu & Okinawa', 'prefectures': format_choices(
                    Activity.KYUSHU_OKINAWA)},
            ]
        })


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('-created_at')
    serializer_class = BookingSerializer
