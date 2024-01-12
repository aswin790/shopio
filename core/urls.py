"""
URL configuration for shopio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.urls import path,include
from django.conf.urls.static import static 
from . import views
from django.conf import settings
from . forms import loginForm
app_name = 'core'

urlpatterns = [
    
    path('',views.home),
    path('signup/',views.user_signup,name = 'signup'),
    path('login/',auth_views.LoginView.as_view(template_name = 'user/login.html',authentication_form = loginForm), name = 'login'),
    path('logout',views.user_logout,name='logout'),
    path('contact/', views.contact, name='contact'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

