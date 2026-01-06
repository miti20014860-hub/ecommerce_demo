from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BannerViewSet, NewsViewSet, NoticeViewSet, QuoteViewSet

router = DefaultRouter()
router.register(r'banners', BannerViewSet, basename='banners')
router.register(r'news', NewsViewSet, basename='news')
router.register(r'notices', NoticeViewSet, basename='notices')
router.register(r'quotes', QuoteViewSet, basename='quotes')

urlpatterns = [
    path('', include(router.urls)),
]