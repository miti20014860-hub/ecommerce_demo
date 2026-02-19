from django.db.models import Q
from rest_framework import viewsets, generics, status
from django.contrib.auth import update_session_auth_hash
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from index.models import Banner, News, Notice, Quote
from activity.models import Activity, Booking
from collection.models import Collection, Order
from kenshi.models import Kenshi
from member.models import Member
from .serializers import BannerSerializer, NewsSerializer, NoticeSerializer, QuoteSerializer, ActivitySerializer, BookingSerializer, CollectionSerializer, OrderSerializer, KenshiSerializer, MemberProfileSerializer, RegisterSerializer, UpdateProfileSerializer, ChangePasswordSerializer


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


# Pagination
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 100


# Activity
class ActivityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Activity.objects.all().order_by('-created_at')
    serializer_class = ActivitySerializer
    pagination_class = StandardResultsSetPagination

    @action(detail=False, methods=['get'])
    def filters(self, request):
        def format_choices(choices):
            return [{'value': x[0], 'label': x[1]} for x in choices]

        return Response({
            'types': format_choices(Activity.TYPE_CHOICES),
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
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        activity_id = self.request.data.get('activity_id')
        activity = Activity.objects.get(id=activity_id)

        serializer.save(
            user=self.request.user if self.request.user.is_authenticated else None,
            title=activity.title,
            activity_obj=activity
        )


# Collection
class CollectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Collection.objects.all().order_by('-created_at')
    serializer_class = CollectionSerializer
    pagination_class = StandardResultsSetPagination

    @action(detail=False, methods=['get'])
    def filters(self, request):
        def format_choices(choices):
            return [{'value': x[0], 'label': x[1]} for x in choices]

        return Response({
            'types': format_choices(Collection.TYPE_CHOICES),
            'period_types': format_choices(Collection.PERIOD_CHOICES),
        })

    def get_queryset(self):
        queryset = Collection.objects.all().order_by('-created_at')

        q = self.request.query_params.get('q', None)
        types = self.request.query_params.getlist('types')
        price_min = self.request.query_params.get('price_min', None)
        price_max = self.request.query_params.get('price_max', None)
        period = self.request.query_params.get('period', None)
        length_min = self.request.query_params.get('length_min', None)
        length_max = self.request.query_params.get('length_max', None)

        if q:
            queryset = queryset.filter(Q(name_jp__icontains=q) | Q(name_en__icontains=q) | Q(provider__icontains=q))
        if types:
            queryset = queryset.filter(type__in=types)
        if price_min:
            queryset = queryset.filter(price__gte=price_min)
        if price_max:
            queryset = queryset.filter(price__lte=price_max)
        if period:
            queryset = queryset.filter(period__in=period)
        if length_min:
            queryset = queryset.filter(price__gte=length_min)
        if length_max:
            queryset = queryset.filter(price__lte=length_max)

        return queryset


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        collection_id = self.request.data.get('collection_id')
        collection = Collection.objects.get(id=collection_id)

        serializer.save(
            user=self.request.user if self.request.user.is_authenticated else None,
            name_jp=collection.name_jp,
            collection_obj=collection
        )


# Kenshi
class KenshiViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Kenshi.objects.all().order_by('-created_at')
    serializer_class = KenshiSerializer


# Member
class MemberProfileView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MemberProfileSerializer

    def get_object(self):
        user = self.request.user
        from member.models import Member
        return Member.objects.prefetch_related('bookings', 'orders').get(id=user.id)


class RegisterView(generics.CreateAPIView):
    queryset = Member.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


class UpdateProfileView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateProfileSerializer

    def get_object(self):
        return self.request.user


class ChangePasswordView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.request.user.set_password(serializer.validated_data['new_password'])
        self.request.user.save()
        return Response({"detail": "Password has been updated."}, status=status.HTTP_200_OK)
