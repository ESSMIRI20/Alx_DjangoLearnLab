from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Like

class LikeTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(title='Test Post', content='Content here', user=self.user)

    def test_like_post(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(f'/posts/{self.post.id}/like/')
        self.assertEqual(response.json()['status'], 'liked')

    def test_unlike_post(self):
        self.client.login(username='testuser', password='12345')
        Like.objects.create(user=self.user, post=self.post)
        response = self.client.post(f'/posts/{self.post.id}/unlike/')
        self.assertEqual(response.json()['status'], 'unliked')

