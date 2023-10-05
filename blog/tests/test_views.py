from django.test import TestCase, Client
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.urls import reverse
from blog.models import Post, UserProfile, GameCategory, Comment
from blog.views import (
    landing_page,
    about,
    contact,
    contactus_success,
    my_articles,
    CategoryView,
    PostList,
    UsersPosts,
    PostDetail,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostLike,
    handler403,
    handler404,
    handler405,
    handler500,
)
from blog.forms import (
    CommentForm, UserForm, PostForm,
    ProfileForm, ContactForm
)
import datetime


class TestViews(TestCase):
    def setUp(self):
        """
        Basic setup for different scenario Test cases
        """
        self.client = Client()

        # Creating a test user
        test_user = User.objects.create_user(
            username="test_user",
            email="test_user@gmail.com",
            password="test_password"
        )
        test_user.is_staff = True
        test_user.is_superuser = True
        test_user.save()
        self.test_user = test_user

        # Creating a test blog post
        self.test_post = Post.objects.create(
            title="Test Post",
            slug="test-post",
            author=self.test_user,
            content="Test content",
            device="Test device",
            category=GameCategory.objects.create(
                name="Test Category",
            ),
        )

        # Creating a test comment
        self.test_comment = Comment.objects.create(
            post=self.test_post, user=self.test_user, body="Test comment body"
        )

    # ==============================
    # User Exist/login/signup
    # ==============================

    def test_user_exists(self):
        """
        Test if a user is created and
        exists in the database
        """
        user_count = get_user_model().objects.count()
        self.assertEqual(user_count, 1)

    def test_login_url(self):
        """
        Test the login URL and user account login
        """
        login_url = settings.LOGIN_URL
        data = {"username": "test_user", "password": "test_password"}
        response = self.client.post("/accounts/login", data, follow=True)
        status_code = response.status_code
        redirect_path = response.get("PATH_INFO")
        self.assertEqual(status_code, 200)

    def test_user_login_successful(self):
        """
        Test the successful login process
        """
        self.client.login(username="test_user", password="test_password")

        # Send a GET request to a protected page (e.g., profile page)
        response = self.client.get(reverse("profile"))

        # Check if the user is redirected after successful login
        self.assertEqual(response.status_code, 200)

        # Check if the user is now logged in
        self.assertTrue(response.context["user"].is_authenticated)

    def test_user_signup_successful(self):
        """
        Test the successful signup process
        """
        # Create a dictionary with user data for signup
        user_data = {
            "username": "test_user",
            "email": "test_user@gmail.com",
            "password1": "test_password",
            "password2": "test_password",
        }

        # Perform a POST request to the signup view with user data
        response = self.client.post(reverse("account_signup"), user_data)

        self.assertEqual(response.status_code, 200)

    # ==============================
    # Post - Create/Update/Delete
    # ==============================

    def test_create_post(self):
        """
        Test the creation of a new post
        """
        self.client.login(username="test_user", password="test_password")

        # Count the number of posts before creating a new one
        initial_post_count = Post.objects.count()

        # Create a new post
        response = self.client.post(
            reverse("post_create"),
            {"title": "Test Post", "content": "New Content"}
        )

        self.assertEqual(response.status_code, 200)

        # Now, check if the post with the title
        # 'New Post' exists in the database
        self.assertTrue(Post.objects.filter(title="Test Post").exists())

    def test_update_post(self):
        """
        Test if update post is successful
        """
        self.client.login(username="test_user", password="test_password")

        # Update the test post
        response = self.client.post(
            reverse("post_update", kwargs={"slug": self.test_post.slug}),
            {"title": "Test Post", "content": "Updated Content"},
        )

        self.assertEqual(response.status_code, 200)

        # Refresh the test_post object from
        # the database to get the updated data
        self.test_post.refresh_from_db()

        # Check if the title of the post has been updated
        self.assertEqual(self.test_post.title, "Test Post")

    def test_delete_post(self):
        """
        Test if delete an existing post is successful
        """
        self.client.login(username="test_user", password="test_password")

        # Delete the test post
        response = self.client.post(
            reverse("post_delete", kwargs={"slug": self.test_post.slug})
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Post.objects.filter(title="Test Post").exists())

    # ==============================
    # Comment - Exist/Create/Delete
    # ==============================

    def test_comment_exists(self):
        """
        Test if existing comment is visible
        """
        comment_count = Comment.objects.filter(pk=self.test_comment.pk).count()
        self.assertEqual(comment_count, 1)

    def test_create_comment(self):
        """
        Test if creating a comment is successful
        """
        self.client.login(username="test_user", password="test_password")

        # Creating a new comment
        response = self.client.post(
            reverse("post_detail", kwargs={"slug": self.test_post.slug}),
            {"body": "Test Comment Body"},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)

        # Check if comment exists in database
        self.assertTrue(
            Comment.objects.filter(body="Test Comment Body").exists()
        )

    def test_comment_delete_redirects_to_post_detail(self):
        """
        Test if user are redirected to post_detail.html
        after deleted comment
        """
        self.client.login(username="test_user", password="test_password")

        # Get the URL for deleting the test comment
        url = reverse("comment_delete", kwargs={"pk": self.test_comment.pk})

        # Send a DELETE request to delete the comment
        response = self.client.delete(url)

        # Check if the response redirects to the post detail page
        self.assertRedirects(
            response,
            reverse("post_detail",
                    kwargs={"slug": self.test_post.slug})
        )

    # ==============================
    # Error handling
    # ==============================

    def test_handler_views(self):
        """
        Test the custom error view, if they are displayed
        """
        response_403 = self.client.get(reverse("handler403"))
        self.assertEqual(response_403.status_code, 403)

        response_404 = self.client.get(reverse("handler404"))
        self.assertEqual(response_404.status_code, 404)

        response_405 = self.client.get(reverse("handler405"))
        self.assertEqual(response_405.status_code, 405)

        response_500 = self.client.get(reverse("handler500"))
        self.assertEqual(response_500.status_code, 500)
