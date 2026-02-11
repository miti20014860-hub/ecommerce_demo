from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
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
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 100


class ActivityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Activity.objects.all().order_by('-created_at')
    serializer_class = ActivitySerializer
    pagination_class = StandardResultsSetPagination

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

    def get_queryset(self):
        queryset = Activity.objects.all().order_by('-created_at')

        q = self.request.query_params.get('q', None)
        types = self.request.query_params.getlist('types')
        charge_min = self.request.query_params.get('charge_min', None)
        charge_max = self.request.query_params.get('charge_max', None)
        event_ends = self.request.query_params.get('event_ends', None)
        prefectures = self.request.query_params.getlist('prefectures')

        if q:
            queryset = queryset.filter(Q(title__icontains=q) | Q(provider__icontains=q) | Q(description__icontains=q))
        if types:
            queryset = queryset.filter(type__in=types)
        if charge_min:
            queryset = queryset.filter(minimum_charge__gte=charge_min)
        if charge_max:
            queryset = queryset.filter(minimum_charge__lte=charge_max)
        if event_ends:
            queryset = queryset.filter(event_ends__gte=event_ends)
        if prefectures:
            queryset = queryset.filter(prefecture__in=prefectures)

        return queryset


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('-created_at')
    serializer_class = BookingSerializer
