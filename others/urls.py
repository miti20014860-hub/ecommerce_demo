from django.urls import path
from . import views

app_name = 'others'

urlpatterns = [
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('terms', views.terms, name='terms'),
    path('privacy', views.privacy, name='privacy'),
    path('faq', views.faq, name='faq'),
]