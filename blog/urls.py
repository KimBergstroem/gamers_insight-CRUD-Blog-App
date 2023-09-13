from . import views
from django.urls import path

urlpatterns = [
    path('index', views.PostList.as_view(), name='index'),
    path('', views.landing_page, name='landing_page'),
    path('about/', views.about, name='about'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
