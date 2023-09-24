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

    # Password Reset
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name='password_reset_complete'),

    # Password Change
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='account/password_change.html'), name='password_change'),
    path('password-change/done', auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'), name='password_change_done'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = 'blog.views.handler403'
handler404 = 'blog.views.handler404'
handler405 = 'blog.views.handler405'
handler500 = 'blog.views.handler500'
