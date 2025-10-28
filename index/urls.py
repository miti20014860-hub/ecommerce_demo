from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
    path('', views.index, name='index'),
    path('news/<int:pk>/', views.news, name='news'),
    path('notice/<int:pk>/', views.notice, name='notice'),
    path('about', views.about, name='about'),
    path('privacy', views.privacy, name='privacy'),
    path('contact', views.contact, name='contact'),
    path('terms', views.terms, name='terms'),
    path('faq', views.faq, name='faq'),
]
