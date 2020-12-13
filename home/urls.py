from django.urls import path
from .views import (
    IndexFormView,
    AboutTemplateView,
    ContactTemplateView,
)

urlpatterns = [
    path('', IndexFormView.as_view(), name='index'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('contact/', ContactTemplateView.as_view(), name='contact'),
]
