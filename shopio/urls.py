# main urls.py
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('inbox/',include('conversation.urls')),
    path('Item/', include('item.urls', namespace='Item')),  # Use 'Item' as the namespace
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

