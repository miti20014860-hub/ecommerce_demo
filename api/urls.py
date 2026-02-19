from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import BannerViewSet, NewsViewSet, NoticeViewSet, QuoteViewSet, ActivityViewSet, BookingViewSet, CollectionViewSet, OrderViewSet, KenshiViewSet, MemberProfileView, RegisterView, UpdateProfileView, ChangePasswordView

router = DefaultRouter()
router.register(r'banners', BannerViewSet, basename='banner')
router.register(r'news', NewsViewSet, basename='news')
router.register(r'notices', NoticeViewSet, basename='notice')
router.register(r'quotes', QuoteViewSet, basename='quote')
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'bookings', BookingViewSet, basename='booking')
router.register(r'collections', CollectionViewSet, basename='collection')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'kenshi', KenshiViewSet, basename='kenshi')

urlpatterns = [
    path('', include(router.urls)),
    path('sign_in/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('sign_in/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('sign_up/', RegisterView.as_view(), name='auth_register'),
    path('profile/', MemberProfileView.as_view(), name='member_profile'),
    path('profile/update/', UpdateProfileView.as_view(), name='profile_update'),
    path('profile/change_password/', ChangePasswordView.as_view(), name='change_password'),
]
