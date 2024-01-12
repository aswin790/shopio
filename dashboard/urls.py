from django.urls import path
from django.conf.urls.static import static 
from . import views
from django.conf import settings
app_name = 'dashboard'

urlpatterns = [
    
    path('dashboars/',views.dashboard,name='dashboard'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)