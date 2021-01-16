from django.urls import path
from django.contrib.auth import views as auth_views
from .decorators import is_authenticated
from .views import (
    IndexFormView,
    AboutTemplateView,
    ContactView,
    UserResgistrationCreateView,
    UserLoginView
)

urlpatterns = [
    path('', IndexFormView.as_view(), name='index'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('auth/register/', UserResgistrationCreateView.as_view(), name='register'),
    path('auth/login/', UserLoginView.as_view(), name='login'),
    path('auth/logout/', auth_views.LogoutView.as_view(template_name='home/auth/logout.html'), name='logout'),
]
