from django.urls import path
from . import views

app_name = 'member'

urlpatterns = [
    path('', views.member, name='member'),
    path('account', views.account, name='account'),
    path('sing_in', views.sing_in, name='sing_in'),
    path('sing_up', views.sing_up, name='sing_up'),
    path('profile', views.profile, name='profile'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('change_password', views.change_password, name='change_password'),
]
