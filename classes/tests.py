from django.test import TestCase
from rest_framework.test import APIClient
from classes.models import ClassRoom
from django.contrib.auth import get_user_model

# Create your tests here.
from unittest.mock import patch
from faker import Faker

User = get_user_model()


class ClassesTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            Faker.name(), Faker.email(), Faker.password()
        )
        return super().setUp()

    def test_something(self):
        self.client.get("/api/v1/classes/")
        classes = ClassRoom.objects.all()
        self.assertEqual(len(classes), 2)

    @patch("classes.models.ClassRoom.objects")
    def test_mocking(self, mock_class):
        mock_class.all.return_value = 3
        classes = ClassRoom.objects.all()
        self.assertEqual(classes, 3)
