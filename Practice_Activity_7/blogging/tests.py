from django.test import TestCase
from django.contrib.auth.models import User
from blogging.models import Post, Category
import datetime
from datetime import timezone


class CategoryTestCase(TestCase):
    """Unit tests for the Category model"""

    def test_string_representation(self):
        expected = "A Category"
        c1 = Category(name=expected)
        self.assertEqual(str(c1), expected)


class FrontEndTestCase(TestCase):
    """Functional tests for the public blog views"""
    fixtures = ['blogging_test_fixture.json', ]

    def setUp(self):
        
        self.now = datetime.datetime.now(tz=timezone.utc)
        self.timedelta = datetime.timedelta(15)

        author = User.objects.get(pk=1)

        
        for i in range(1, 11):
            p = Post(title=f"Post {i} Title", text="foo", author=author)
            if i < 6:
                p.published_date = self.now - self.timedelta * i
            p.save()

    def test_list_only_published(self):
        """Home page should list only published posts"""
        resp = self.client.get('/')
        resp_text = resp.content.decode(resp.charset)

        
        self.assertIn("Recent Posts", resp_text)

        for i in range(1, 11):
            title = f"Post {i} Title"
            if i < 6:
                
                self.assertContains(resp, title, count=1)
            else:
               
                self.assertNotContains(resp, title)

    def test_details_only_published(self):
        """Detail page returns 200 for published, 404 for unpublished"""
        for i in range(1, 11):
            post = Post.objects.get(title=f"Post {i} Title")
            resp = self.client.get(f'/posts/{post.pk}/')
            if i < 6:
                self.assertEqual(resp.status_code, 200)
                self.assertContains(resp, post.title)
            else:
                self.assertEqual(resp.status_code, 404)
