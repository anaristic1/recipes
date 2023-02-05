from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_email_user_successful(self):
        email = 'test@example.com'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password, password)

    def test_new_user_email_normalized(self):
        sample_emails = [
            ['test1@SAMPLE.COM', 'test1@sample.com'],
            ['Test2@Sample.com', 'Test2@sample.com'],
            ['TEST3@SAMPLE.COM', 'TEST3@sample.com'],
            ['test4@sample.COM', 'test4@sample.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email=email, password='sample123')
            self.assertEqual(user.email, expected)

    def test_create_user_without_email_raises_error(self):
        with self.assertRaises(ValueError):
            user = get_user_model().objects.create_user(email='', password='sample123')

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            email='test@sample.com', password='sample123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
