from django.urls import path
from . import views

app_name = 'iai'

urlpatterns = [
    path('', views.iai, name='iai'),
]
