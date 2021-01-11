from django.urls import path
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
]
