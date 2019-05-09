from django.test import TestCase
from .models import *

from django.test import Client

from URLShortener.settings import SHORT_URL_LENGHT,DOMAIN


class ShortURL_Test(TestCase):
    def setUp(self):

        ShortURL.objects.create(original="http://www.google.com", short="2aze5h")
        print ("Url lenght is {} characters long.".format(SHORT_URL_LENGHT))

        
    def test_URL_path(self):

        obj = ShortURL.objects.get(short="2aze5h")
        self.assertEqual(obj.short,"2aze5h")

        response = Client().post('', {'original': 'https://twitter.com/elonmusk'})
        self.assertEqual(response.status_code,200)

        response =  Client().get('/go/2aze5h')
        self.assertEqual(response.status_code,302 or 301)
        
        response =  Client().get('/go/112233')
        self.assertEqual(response.status_code,200)
        
        
        response =  Client().get('')
        self.assertEqual(response.status_code,200)

   