from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from blog.views import (
    landing_page,
    about,
    contact,
    contactus_success,
    my_articles,
    CategoryView,
    PostLike,
)
from blog.models import Post, GameCategory, Comment


class TestUrls(TestCase):
    """
    Test cases for URLs to their corresponding view functions
    Blog/urls.py against the corresponding blog/views.py
    """

    def setUp(self):
        """
        Basic setup for making test user and creating post
        for postlike/comment view
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

    def test_landing_page_url_resolves(self):
        """
        Test if the URL for the Landing page correctly
        resolves to the 'landing_page' view function.
        """
        url = reverse("landing_page")
        self.assertEqual(resolve(url).func, landing_page)

    def test_about_url_resolves(self):
        """
        Test if the URL for the About correctly
        resolves to the 'about' view function.
        """
        url = reverse("about")
        self.assertEqual(resolve(url).func, about)

    def test_contact_url_resolves(self):
        """
        Test if the URL for the Contact correctly
        resolves to the 'contactus' view function.
        """
        url = reverse("contact")
        self.assertEqual(resolve(url).func, contact)

    def test_contactus_success_url_resolves(self):
        """
        Test if the URL for the Contact Success correctly
        resolves to the 'contactus_success' view function.
        """
        url = reverse("contactus_success")
        self.assertEqual(resolve(url).func, contactus_success)

    def test_my_articles_url_resolves(self):
        """
        Test if the URL for the My articles correctly
        resolves to the 'my_articles' view function.
        """
        url = reverse("my_articles")
        self.assertEqual(resolve(url).func, my_articles)

    def test_category_view_url_resolves(self):
        """
        Test if the URL for the category view correctly
        resolves to the 'index.html' view function with
        the associated category 1,2 or 3.
        """
        category_ids = [1, 2, 3]
        for category_id in category_ids:
            url = reverse("category", args=[category_id])
            self.assertEqual(resolve(url).func, CategoryView)

    def test_post_like_url_resolves(self):
        """
        Test if the URL for liking a post correctly
        resolves to the 'PostLike' view function.
        """
        url = reverse("post_like", kwargs={"slug": "test-post"})
        self.assertEqual(resolve(url).func.view_class, PostLike)
