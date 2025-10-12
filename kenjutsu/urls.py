from django.urls import path
from . import views

app_name = 'kenjutsu'

urlpatterns = [
    path('', views.kenjutsu, name='kenjutsu'),
]
