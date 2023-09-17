from .models import Comment, UserProfile, Post, GameCategory
from django import forms
from django.contrib.auth.models import User

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

# Making it to an python list
choices = GameCategory.objects.all().values_list('name','name')
choice_list = []
for item in choices:
    choice_list.append(item)

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
            'category': forms.Select(choices=choice_list, attrs={ 'class': 'form-control'}),
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