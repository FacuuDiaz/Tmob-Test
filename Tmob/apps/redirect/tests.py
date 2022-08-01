from django.test import TestCase,Client
from django.contrib.auth.models import User
from apps.redirect.models import Redirect
from django.core.cache import cache
import json
# Create your tests here.
class RedirectServiceTestCase(TestCase):
    client = Client()
    url = "/redirects"
    def login(self) -> None:
        return self.client.login(username='test',password='test')

    def setUp(self) -> None:
        # Creating test user for fetch endpoint services
        user = User.objects.create(username='test')
        user.set_password('test')
        user.save()


        self.example_1 = Redirect.objects.create(key="1",url="localhost:8000",active=True)
        self.example_2 = Redirect.objects.create(key="2",url="localhost:8100",active=True)
        self.example_3 = Redirect.objects.create(key="3",url="localhost:8200",active=True)
        self.example_4 = Redirect.objects.create(key="4",url="localhost:8400",active=True)

        self.example_1.save()
        self.example_2.save()
        self.example_3.save()
        self.example_4.save()


    def test_redirect_correct_response(self) -> None:
        self.login()
        path = f"{self.url}/1"
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(content["key"], "1")
        self.assertEqual(content["url"], "localhost:8000" )
    
    def test_redirect_incorrect_response(self) ->None:
        self.login()
        path = f"{self.url}/20"
        response = self.client.get(path)
        self.assertEqual(response.status_code, 409)
        self.assertEqual(type(response.content),bytes)
        self.assertEqual(response.content,b"Don't exist a Redirect instance with this key: '20'. \n Try again with another key")

class RedirectModelTestCase(TestCase):

    def setUp(self):
        self.redirect_1 = Redirect.objects.create(key="1",url="localhost:8000",active=True)
        self.redirect_2 = Redirect.objects.create(key="2",url="localhost:9000",active=True)
        self.redirect_1.save()
        self.redirect_2.save()

    def test_get_instance_with_key(self) -> None:
        #Correct Case
        response = Redirect.get_instance_with_key(self.redirect_1.key)
        self.assertEqual(response['key'],self.redirect_1.key)
        self.assertEqual(response['url'],self.redirect_1.url)

        #Incorrect Case
        response = Redirect.get_instance_with_key("3")
        self.assertEqual(response,None)

    
    def test_get_redirect(self):
        #cached
        response = Redirect.get_redirect(self.redirect_1.key)
        self.assertEqual(response['key'],self.redirect_1.key)
        self.assertEqual(response['url'],self.redirect_1.url)
        
        #updating
        self.redirect_1.url = "newurl:8000"
        self.redirect_1.active = False
        self.redirect_1.save()

        #uncached
        self.assertEqual(cache.get(self.redirect_1.key),None)

        #direct request
        response = Redirect.get_redirect(self.redirect_1.key)
        self.assertEqual(response['key'],self.redirect_1.key)
        self.assertEqual(response['url'],self.redirect_1.url)