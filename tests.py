from django.test import TestCase
from django.contrib.auth.models import User
from blogging.models import Post
class PostTestCase(TestCase):
    fixtures = ['blogging_test_fixture.json']
    def setUp(self):
        self.user = User.objects.get(pk=1)
    def test_str_returns_title(self):
        p = Post.objects.create(title='Hello', text='Body', author=self.user)
        self.assertEqual(str(p), 'Hello')
