from django.test import TestCase
from blog.models import UserProfile, GameCategory, Post, Comment
from django.contrib.auth.models import User


class TestModels(TestCase):
    """
    Test cases for models in the blog app
    """
    def setUp(self):
        """
        Set up initial data for testing
        """
        # Create a test user
        self.test_user = User.objects.create_user(username='test_user', password='test_password')
        
        # Create a test game category
        self.test_category = GameCategory.objects.create(name='Test Category')
       
        # Create a test post
        self.test_post = Post.objects.create(
            content='Test Content',
            excerpt='Test Excerpt',
            title='Test Title',
            status=1,  # Published
            author=self.test_user,
            category=self.test_category,
            device='PC'
        )


    def test_user_profile_creation(self):
        """
        Test if a user profile is created when a user is created
        """
        self.assertTrue(UserProfile.objects.filter(user=self.test_user).exists())


    def test_game_category_creation(self):
        """
        Test if a game category is created successfully
        """
        category = GameCategory.objects.create(name='Test Category')
        self.assertEqual(category.name, 'Test Category')


    def test_post_creation(self):
        """
        Test if a post is created successfully
        """
        self.assertEqual(self.test_post.title, 'Test Title')
        self.assertEqual(self.test_post.author, self.test_user)
        self.assertEqual(self.test_post.category, self.test_category)


    def test_comment_creation(self):
        """
        Test if a comment is created successfully
        """
        # Create a test comment
        comment = Comment.objects.create(
            body='Test Comment',
            approved=True,
            post=self.test_post,
            user=self.test_user
        )
        self.assertEqual(comment.body, 'Test Comment')
        self.assertTrue(comment.approved)
        self.assertEqual(comment.post, self.test_post)
        self.assertEqual(comment.user, self.test_user)
