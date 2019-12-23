from django.test import TestCase

# Create your tests here.

from .models import Post

class PostTest(TestCase):
    def setUp(self):
        Post.objects.create(text = 'just a test')
    
    def test_text_content(self):
        post = Post.objects.get(id = 1)
        expect = f'{post.text}'
        self.assertEqual(expect, 'just a test')

class HomepageTest(TestCase):
    def setUp(self):
        Post.objects.create(text = 'this is another smaple')
    def one(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)

    def two(self):
        res = self.client.get(reverse('post'))
        self.assertEqual(res_status_code, 200)
        self.assertTemplateUsed(res, 'about.html')
