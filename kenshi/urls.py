from django.urls import path
from . import views

app_name = 'kenshi'

urlpatterns = [
    path('', views.kenjutsuka, name='kenshi'),
]
