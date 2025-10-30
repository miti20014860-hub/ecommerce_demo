from django.urls import path
from . import views

app_name = 'collection'

urlpatterns = [
    path('', views.collection, name='collection'),
    path('item/', views.item, name='item'),
    path('form/', views.order_form, name='order_form'),
    path('order_form', views.order_form, name='order_form'),
]
