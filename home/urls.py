from django.urls import path
from django.contrib.auth import views as auth_views
from .decorators import is_authenticated
from .views import (
    IndexFormView,
    AboutTemplateView,
    ContactView,
    UserResgistrationCreateView,
)

urlpatterns = [
    path('', is_authenticated(IndexFormView.as_view()), name='index'),
    path('about/', is_authenticated(AboutTemplateView.as_view()), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('auth/register/', is_authenticated(UserResgistrationCreateView.as_view()), name='register'),
    path('auth/login/', is_authenticated(auth_views.LoginView.as_view(template_name='home/auth/login.html')), name='login'),
    path('auth/logout/', auth_views.LogoutView.as_view(template_name='home/auth/logout.html'), name='logout'),
]
