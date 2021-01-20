from django.urls import path
from .views import (
    BlogListView, TaggedPostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView
)

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('post/tag/<slug:slug>/', TaggedPostListView.as_view(), name='tag'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post'),
    path('new/post/', PostCreateView.as_view(), name='add-post'),
    path('post/update/<slug:slug>/', PostUpdateView.as_view(), name='update-post'),
    path('post/delete/<slug:slug>/', PostDeleteView.as_view(), name='delete-post'),
]
