from .models import Comment, UserProfile, Post, GameCategory
from django import forms
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CommentForm(forms.ModelForm):
    """
    Comment form in blog posts
    """
    class Meta:
        """
        Form fields
        """
        model = Comment
        fields = ('body',)

    body = forms.CharField(max_length=300)

class UserForm(forms.ModelForm):
    """
    Form for user registration and profile information
    """
    class Meta:
        """
        Form fields
        """
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]

    username = forms.CharField(max_length=15)
    first_name = forms.CharField(max_length=15)
    last_name = forms.CharField(max_length=15)
    email = forms.EmailField(max_length=40)

class PostForm(forms.ModelForm):
    """
    PostForm for blog posting
    """
    class Meta:
        """
        Form fields
        """
        model = Post
        fields = [
            'title',
            'category',
            'device',
            'featured_image',
            'excerpt',
            'content',
        ]
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'device': forms.Select(attrs={'class': 'form-control'}),
            'content': SummernoteWidget(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Max 50 characters'}),
            'excerpt': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Max 75 characters'}),
        }

class ProfileForm(forms.ModelForm):
    """
    User profile page form
    """
    class Meta:
        """
        Form fields
        """
        model = UserProfile
        fields = [
            'bio',
            'profile_picture',
            'country',
        ]
        widgets = {
            'profile_picture': forms.FileInput(),  # forms.FileInput for
            # custom rendering, removing current url link displayed
        }
