from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Notification

class NotificationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_get_notifications(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get('/notifications/')
        self.assertEqual(response.status_code, 200)
