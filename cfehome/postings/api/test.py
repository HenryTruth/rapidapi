from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

from postings.models import BlogPost
User = get_user_model()

class BlogPostAPITestCase(APITestCase):
    def setup(self):
        user_obj = User(username='testcfeuser', email='test@test.com')
        user_obj.set_password("somerandopassword")
        user_obj.save()
        blog_post = BlogPost.objects.create(
            user=user_obj, title='New title', content='some_random_content'
            )

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_post(self):
        post_count = User.objects.count()
        self.assertEqual(User_count, 1)