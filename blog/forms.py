from .models import Comment, UserProfile, Post, GameCategory
from django import forms
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class CommentForm(forms.ModelForm):
    # Comment form in blog posts
    class Meta:
        model = Comment
        fields = ('body',)


class UserForm(forms.ModelForm):
    # User form
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]


class PostForm(forms.ModelForm):
    # PostForm for blog posting
    class Meta:
        model = Post
        fields = [
            'title', 
            'category', 
            'featured_image', 
            'excerpt', 
            'content',
        ]
        widgets = {
            'category': forms.Select(attrs={ 'class': 'form-control'}),
        }


class ProfileForm(forms.ModelForm):
    # User profile page form
    class Meta:
        model = UserProfile
        fields = [
            'bio',
            'profile_picture',
            'country',
        ]
        widgets = {
            'profile_picture': forms.FileInput(),  # forms.FileInput for custom rendering, removing current url link displayed
        }