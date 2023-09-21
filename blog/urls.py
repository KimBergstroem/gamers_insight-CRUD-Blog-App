from . import views
from django.urls import path
from .views import (
    ProfileUpdateView, ProfileView, ProfileDeleteView,  PostCreateView, PostUpdateView, PostDeleteView, CommentDeleteView, CategoryView
)

urlpatterns = [
    # ==============================
    # Main paths
    # ==============================
    path('', views.landing_page, name='landing_page'),
    path('about/', views.about, name='about'),
    path('contactus/', views.contactus, name='contactus'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),

    # ==============================
    # Profile paths
    # ==============================
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile_update/', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('profile_delete/<int:pk>/', views.ProfileDeleteView.as_view(), name='profile_delete'),

    # ==============================
    # Post paths
    # ==============================
    path('index', views.PostList.as_view(), name='index'),
    path('post_detail/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('post_create/', views.PostCreateView.as_view(), name='post_create'),
    path('post_update/<slug:slug>', views.PostUpdateView.as_view(), name='post_update'),
    path('post_delete/<slug:slug>/delete', views.PostDeleteView.as_view(), name='post_delete'),
    
    # ==============================
    # Comment paths
    # ==============================
    path('comment_delete/<int:pk>/deletecomment/', views.CommentDeleteView.as_view(), name='comment_delete'),

    # ==============================
    # Category paths
    # ==============================
    path('category/<str:genre>/', CategoryView, name='category'),
]