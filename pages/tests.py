from django.test import SimpleTestCase

# Create your tests here.

class SimpleTests(SimpleTestCase):

    def test_homepage_status(self):
        request = self.client.get('/pages/about/')
        self.assertEqual(request.status_code, 200)
    
    def test_aboutpage_status(self):
        request = self.client.get('/pages/home/')
        self.assertEqual(request.status_code, 200)