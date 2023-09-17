from . import views
from django.urls import path
from .views import (
    ProfileUpdateView, ProfileView,  PostCreateView, PostUpdateView, PostDeleteView
)

urlpatterns = [
    path('index', views.PostList.as_view(), name='index'),
    path('', views.landing_page, name='landing_page'),
    path('about/', views.about, name='about'),
    path('contactus/', views.contactus, name='contactus'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('post_detail/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile_update/', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('post_create/', views.PostCreateView.as_view(), name='post_create'),
    path('post_update/<slug:slug>', views.PostUpdateView.as_view(), name='post_update'),
    path('post_delete/<slug:slug>/delete', views.PostDeleteView.as_view(), name='post_delete'),
]