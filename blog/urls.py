from django.urls import path
from .views import (
    BlogListView,
    TaggedPostListView,
    PostDetailView,
    PostCreateView
)

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('tag/<slug:slug>/', TaggedPostListView.as_view(), name='tag'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post'),
    path('new/post/', PostCreateView.as_view(), name='add-post'),
]
