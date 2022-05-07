from django.urls import path
from .views import (
    HomePageView, 
    BlogDetailView, 
    BlogCreateView, 
    BlogEditView, 
    BlogDeleteView
    )

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('post/<int:pk>/',BlogDetailView.as_view(),name='post_detail'),
    path('post/create/',BlogCreateView.as_view(),name='post_create'),
    path('post/<int:pk>/edit/',BlogEditView.as_view(),name='post_edit'),
    path('post/<int:pk>/delete/',BlogDeleteView.as_view(),name='post_delete'),
]
