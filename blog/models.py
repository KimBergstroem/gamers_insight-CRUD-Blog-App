from django.db import models
from django.contrib.auth.models import User 
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from django.urls import reverse


STATUS = ((0, "Draft"), (1, "Published"))

# ==============================
# Profile Model
# ==============================
class UserProfile(models.Model):
    """
    Database model for user's profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=150, blank=True)
    username = models.CharField(max_length=15, default="User")
    first_name = models.CharField(max_length=15, default="Usef")
    last_name = models.CharField(max_length=15, default="Usefsson")
    email = models.EmailField(max_length=40, default="User@game-insight.com")
    profile_picture = CloudinaryField(
        'image',
        default=("https://res.cloudinary.com/dpwnz6ieo/image/upload/"
                 "v1694794787/"
                 "illustration-user-avatar-icon_53876-5907_uvdvsz.avif"),
        blank=True,
    )
    country = models.CharField(
        max_length=30, default="Citizen of the Cyber world", blank=True
    )

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        """
        If a user are created from the built in
        django user model, then this profile will be linked
        to that user
        """
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        """
        Save the user profile when the associated User instance is saved
        """
        instance.userprofile.save()

    def __str__(self):
        """
        Returns a string representation of the user's profile
        by using their username
        """
        return self.user.username


# ==============================
# Category Model
# ==============================
class GameCategory(models.Model):
    """
    Database model for game categories
    """
    name = models.CharField(max_length=25)

    def __str__(self):
        """
        Returns a string representation of a category name
        """
        return self.name

    def get_absolute_url(self):
        """
        Returns the absolute URL for the GameCategory instance
        """
        return reverse("index")


# ==============================
# Post Model
# ==============================
class Post(models.Model):
    """
    Database model for posts
    """
    content = models.TextField(max_length=2000, blank=True)
    excerpt = models.TextField(max_length=75, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    title = models.CharField(max_length=50, unique=True)
    status = models.IntegerField(choices=STATUS, default=1)
    featured_image = CloudinaryField("image", default="placeholder")
    likes = models.ManyToManyField(User, related_name="blog_likes", blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    category = models.ForeignKey(
        GameCategory, on_delete=models.CASCADE, default=None
    )
    DEVICE_CHOICES = (
        ("PC", "PC"),
        ("Nintendo", "Nintendo"),
        ("Xbox", "Xbox"),
        ("PlayStation", "PlayStation"),
    )

    device = models.CharField(
        max_length=20, choices=DEVICE_CHOICES, default=None
    )

    class Meta:
        """
        Set the order of posts by date descending
        """

        ordering = ["-created_on"]

    def __str__(self):
        """
        Returns a string representation of an object
        """
        return self.title

    def number_of_likes(self):
        """
        Returns number of blog post likes
        """
        return self.likes.count()

    def get_absolute_url(self):
        """
        For be able to update the blogpost and redirect user back to home page
        """
        return reverse("index")


# ==============================
# Comment Model
# ==============================
class Comment(models.Model):
    """
    Database model for comments
    """
    body = models.TextField(max_length=300)
    approved = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=12)

    class Meta:
        """
        Sets the order of comments by date ascending
        """
        ordering = ["created_on"]

    def __str__(self):
        """
        Returns comment with body and name
        """
        return f"Comment {self.body} by {self.name}"
