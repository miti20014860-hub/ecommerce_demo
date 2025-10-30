from django.urls import path
from . import views

app_name = 'activities'

urlpatterns = [
    path('', views.activities, name='activities'),
    path('<int:pk>/', views.plan, name='plan'),
    path('booking/<int:pk>/', views.booking_view, name='booking_view'),
]
