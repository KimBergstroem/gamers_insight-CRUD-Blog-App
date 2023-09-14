from . import views
from django.urls import path

urlpatterns = [
    path('index', views.PostList.as_view(), name='index'),
    path('', views.landing_page, name='landing_page'),
    path('about/', views.about, name='about'),
    path('contactus/', views.contactus, name='contactus'),
    path('profile/', views.profile, name='profile'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
