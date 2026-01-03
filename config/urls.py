from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('api/', include('api.urls')),
    path('', include('index.urls', namespace='index')),
    path('activity/', include('activity.urls', namespace='activity')),
    path('collection/', include('collection.urls', namespace='collection')),
    path('kenshi/', include('kenshi.urls', namespace='kenshi')),
    path('member/', include('member.urls', namespace='member')),
    path('others/', include('others.urls', namespace='others')),
    path('admin/', admin.site.urls),
] + debug_toolbar_urls() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)