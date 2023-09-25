from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # ==============================
    # App urls paths
    # ==============================
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('blog.urls'), name='blog_urls'),
    path('accounts/', include('allauth.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = 'blog.views.handler403'
handler404 = 'blog.views.handler404'
handler405 = 'blog.views.handler405'
handler500 = 'blog.views.handler500'
