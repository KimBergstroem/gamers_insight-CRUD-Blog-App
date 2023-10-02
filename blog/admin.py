from django.contrib import admin
from .models import Post, Comment, UserProfile, GameCategory
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(UserProfile)
admin.site.register(GameCategory)


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Post model in admin panel
    """
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Comment model in admin panel
    """
    list_display = ('user', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('user__username', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
        Approve user comments
        """
        queryset.update(approved=True)
