from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
    path('', views.index, name='index'),
    path('news/<int:pk>/', views.news, name='news'),
    path('notice/<int:pk>/', views.notice, name='notice'),
]
