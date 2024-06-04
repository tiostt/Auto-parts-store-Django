from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from app import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', include('main.urls', namespace='main')),
    path('catalog/', include('catalog.urls', namespace='catalog')),
    path('user/', include('users.urls', namespace='user')),
    path('basket/', include('basket.urls', namespace='basket')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)