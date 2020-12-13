from django.urls import path
from .views import (
    IndexFormView,
    AboutTemplateView,
)

urlpatterns = [
    path('', IndexFormView.as_view(), name='index'),
    path('about/', AboutTemplateView.as_view(), name='about'),
]
