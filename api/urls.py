from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import QuotesListAPIView
router = DefaultRouter()

urlpatterns = [
    path('quotes/', QuotesListAPIView.as_view(), name='quotes-list'),
    path('api/', include(router.urls)),
    path('api/news/', views.QuotesListAPIView.as_view()),
]