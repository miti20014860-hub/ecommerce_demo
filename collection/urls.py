from django.urls import path
from . import views

app_name = 'collection'

urlpatterns = [
    path('', views.collection, name='collection'),
    path('<int:pk>', views.item, name='item'),
    path('order_form/<int:pk>', views.order_form, name='order_form'),
]
