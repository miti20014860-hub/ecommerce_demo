from django.urls import path
from . import views

app_name = 'member'

urlpatterns = [
    path('', views.member, name='member'),
    path('account/', views.account, name='account'),
    path('account/sign_in/', views.account_sign_in, name='account_sign_in'),
    path('account/sign_up/', views.account_sign_up, name='account_sign_up'),
    path('account/sign_out/', views.account_sign_out, name='account_sign_out'),
]
