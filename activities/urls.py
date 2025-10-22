from django.urls import path
from . import views

app_name = 'activities'

urlpatterns = [
    path('', views.activities, name='activities'),
    path('plan', views.plan, name='plan'),
]
