"""accountmanager1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from .views import SignupView,LoginView,DashboardView,signout
from django.contrib.auth.views import (
    PasswordResetView,PasswordResetConfirmView, PasswordResetDoneView,PasswordResetCompleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',SignupView.as_view(),name='signup'),
    path('login/',LoginView.as_view(),name='login'),
    path('dashboard/',DashboardView.as_view(),name='dashboard'),
    path('logout/',signout,name='signout'),
    path('expenses/',include('expenses.urls')),
    path('income/',include('income.urls')),
    path('reset-password/',PasswordResetView.as_view(),name='forget_password'),
    path('reset-password/confirmation/<str:uidb64>/<str:token>/',PasswordResetConfirmView.as_view(template_name='change_password.html'),name='password_reset_confirm'),
    path('reset-password/done/',PasswordResetDoneView.as_view(template_name='password_done.html'),name='password_reset_done'),
    path('reset-password/complete/',PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='passwore_reset_complete'),
    path('api/',include('api.urls'))



]
