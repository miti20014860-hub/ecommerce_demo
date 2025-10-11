from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home, name='home'),  # 當訪問根路徑時，調用 views.home
]
