from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import BannerListAPIView, QuotesListAPIView
router = DefaultRouter()

urlpatterns = [
    path('banner/', BannerListAPIView.as_view(), name='banner-list'),
    path('quotes/', QuotesListAPIView.as_view(), name='quotes-list'),
    path('api/', include(router.urls)),
    path('api/news/', views.QuotesListAPIView.as_view()),
]