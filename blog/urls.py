from . import views
from django.urls import path
from .views import (
    ProfileUpdateView, ProfileView
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
]