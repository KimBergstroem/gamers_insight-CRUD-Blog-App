from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


STATUS = ((0, "Draft"), (1, "Published"))


# ==============================
# Profile Model
# ==============================
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = CloudinaryField('image', default='https://res.cloudinary.com/dpwnz6ieo/image/upload/v1694794787/illustration-user-avatar-icon_53876-5907_uvdvsz.avif', blank=True)
    country = models.CharField(max_length=200, default='Citizen of the Cyber world', blank=True)

    # If a user are created from the built in django user model, then this profile will be linked to that user.
    @receiver(post_save, sender=User) 
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()

    def __str__(self):
        return self.user.username


# ==============================
# Post Model
# ==============================
class Post(models.Model):
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    title = models.CharField(max_length=200, unique=True)
    status = models.IntegerField(choices=STATUS, default=1)
    featured_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    category = models.CharField(max_length=200, default='Unspecified')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()
    
    # For be able to update the blogpost and redirect user back to home page
    def get_absolute_url(self):
        return reverse('index')


# ==============================
# Comment Model
# ==============================
class Comment(models.Model):  
    body = models.TextField()
    email = models.EmailField()
    name = models.CharField(max_length=80)
    approved = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ['created_on']
    
    def __str__(self):
        return f"Comment {self.body} by {self.name}"


# ==============================
# Category Model
# ==============================
class GameCategory(models.Model):
    name = models.CharField(max_length=200)
    device = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('index')