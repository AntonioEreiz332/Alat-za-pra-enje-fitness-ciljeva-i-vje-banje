"""
URL configuration for mysite project.

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
from django.contrib.auth import views as auth_views
from django.urls import path
from main import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
    path('', views.home, name='home'),  # Ovo je URL za 'home'
   
    # ListView
    path('vjezbe/', views.VjezbaListView.as_view(), name='vjezba_list'),
    path('ciljevi/', views.FitnessCiljListView.as_view(), name='fitnesscilj_list'),
    path('profili/', views.KorisnickiProfilListView.as_view(), name='korisnickiprofil_list'),
    
    # DetailView
    path('vjezba/<int:pk>/', views.VjezbaDetailView.as_view(), name='vjezba_detail'),
    path('cilj/<int:pk>/', views.FitnessCiljDetailView.as_view(), name='fitnesscilj_detail'),
     path('profili/<int:pk>/', views.KorisnickiProfilDetailView.as_view(), name='korisnickiprofil_detail'),
]
