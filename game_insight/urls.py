from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # ==============================
    # App urls paths
    # ==============================
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('blog.urls'), name='blog_urls'),
    path('accounts/', include('allauth.urls')),
]

handler403 = 'blog.views.handler403'
handler404 = 'blog.views.handler404'
handler405 = 'blog.views.handler405'
handler500 = 'blog.views.handler500'
