from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BannerViewSet, NewsViewSet, NoticeViewSet, QuoteViewSet, ActivityViewSet, BookingViewSet, CollectionViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'banners', BannerViewSet, basename='banner')
router.register(r'news', NewsViewSet, basename='news')
router.register(r'notices', NoticeViewSet, basename='notice')
router.register(r'quotes', QuoteViewSet, basename='quote')
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'bookings', BookingViewSet, basename='booking')
router.register(r'collections', CollectionViewSet, basename='collection')
router.register(r'Orders', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]
