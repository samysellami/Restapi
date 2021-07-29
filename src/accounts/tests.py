from django.test import TestCase

from django.contrib.auth import get_user_model

User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username = 'samy', email = 'samy.sellami@hotmail.com')
        user.set_password('requiem')
        user.save()

    def test_created_user(self):
        qs = User.objects.filter(username = 'samy')
        self.assertEqual(qs.count(), 1)