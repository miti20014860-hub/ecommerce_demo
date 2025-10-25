from django.urls import path
from . import views

app_name = 'member'

urlpatterns = [
    path('', views.member, name='member'),
    path('account/', views.account, name='account'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_out', views.sign_out, name='sign_out'),
]
