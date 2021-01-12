from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    IndexFormView,
    AboutTemplateView,
    ContactTemplateView,
    UserResgistrationCreateView,
)

urlpatterns = [
    path('', IndexFormView.as_view(), name='index'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('contact/', ContactTemplateView.as_view(), name='contact'),
    path('auth/register/', UserResgistrationCreateView.as_view(), name='register'),
    path('auth/login/', auth_views.LoginView.as_view(template_name='home/auth/login.html'), name='login'),
    path('auth/logout/', auth_views.LogoutView.as_view(template_name='home/auth/logout.html'), name='logout'),
]
