from django.test import TestCase

from django.contrib.auth import get_user_model
from .models import Status
User = get_user_model()

class StatusTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username = 'samy', email = 'samy.sellami@hotmail.com')
        user.set_password('requiem')
        user.save()

    def test_creating_status(self):
        user = User.objects.get(username = 'samy')
        obj = Status.objects.create(user  = user, content = 'some new content')
        self.assertEqual(obj.id, 1)
        qs = Status.objects.all()
        self.assertEqual(qs.count(), 1)