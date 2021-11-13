from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

app_name = 'app_users'

urlpatterns = [
    path(
        '',
        views.LoginView.as_view(), 
        name = 'login'
    ),
    path(
        'logout/',
        LogoutView.as_view(), 
        name = 'logout'
    ),
    path(
        'profile/<pk>',
        views.ProfileView.as_view(), 
        name = 'profile'
    ),
    path(
        'dashboard/',
        views.Dashboard.as_view(), 
        name = 'dashboard'
    )
]