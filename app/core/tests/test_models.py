from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        """Test creating a user with email is successfull"""
        email = "yoga@yoga.com"
        password = "T3stP4ssw0rd"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
    
    def test_user_email_is_normalized(self):
        '''Test the email for the new user is normalized'''
        email = "gyogarajaeee@GMAIL.COM"
        user = get_user_model().objects.create_user(email=email, password="test123")
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        '''Test creating new user with no email is raising error'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_super_user(self):
        """Test creating a superuser"""
        user = get_user_model().objects.create_superuser(
            email="gyogarajaeee@gmail.com",
            password="test123"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
