"""Test for Django admin modifications"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):
    """Tests for Django admin"""

    # Python unit test module uses camel case
    def setUp(self):
        """Create user and client."""

        self.client = Client()
        self.admin_user = get_user_model().objects.create_user(
            email='user2@exmaple.com',
            password='password123',
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user3@exmaple.com',
            password='password123',
            name='Test user',
        )

    def test_users_list(self):
        """Test that users are listed on page"""

        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)