"""
URL configuration for rs_systems project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views 
from django.contrib.auth.views import LogoutView  
from rs_systems.views import logout_view, home
<<<<<<< HEAD

urlpatterns = [
    path('', views.home, name='home'),  
=======
from rest_framework.authtoken import views as drf_views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('', views.home, name='home'),  
    path('api/', include('apps.technician_portal.api.urls')),
    path('admin/register-technician/', views.register_technician, name='register_technician'),
>>>>>>> 7e7f4cf (Updated technician portal with repair management functionality)
    path('admin/', admin.site.urls),
    path('technician/', include('apps.technician_portal.urls')),
    path('accounts/login/', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
<<<<<<< HEAD
=======
    # path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'),
>>>>>>> 7e7f4cf (Updated technician portal with repair management functionality)
]
