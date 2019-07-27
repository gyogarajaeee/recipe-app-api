from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models

def sample_user(email='yoga@test.com', password='test123'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)

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
        user = get_user_model().objects.create_user(email=email,
                                            password="test123")
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

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name="Vegan"
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingerdient_str(self):
        """ Test the ingredient sting respresentation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)