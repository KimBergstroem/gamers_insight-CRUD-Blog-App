from django.test import TestCase
from .models import User, Post, UserProfile, Comment
import datetime


class TestModels(TestCase):

    def setUp(self):
        test_user = User.objects.create_user(
            username='test_user',
            email='test_user@gmail.com',
            password='test_password'
        )
        test_user.is_staff = True
        test_user.is_superuser = True
        test_user.save()
        self.test_user = test_user
        test_profile = Profile.objects.create(
            id=1,
            user=test_user,
            first_name='test first name',
            last_name='test last name',
            bio='test bio'
        )
        test_post = Post.objects.create(
            id=1,
            title='test title',
            slug='test_title',
            author=test_user,
            content='test content',
        )
        test_post.likes.set([])
        test_comment = Comment.objects.create(
            id=1,
            post=test_post,
            body='test comment body',
            created_on=datetime.date.today(),
            approved=False
        )

    def test_profile_model_returns_str(self):
        user = User.objects.get(
            username='test_user'
        )
        self.assertEqual(
            str(user.username),
            'test_user'
        )

    def test_post_model_returns_str(self):
        post = Post.objects.get(
            title='test title'
        )
        self.assertEqual(
            str(post.title),
            'test title'
        )

    def test_comment_model_returns_str(self):
        comment = Comment.objects.get(
            body='test comment body'
        )
        self.assertEqual(
            str(comment.body),
            'test comment body'
        )