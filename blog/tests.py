import requests
from django.test import TestCase

# Create your tests here.
request = requests.get("http://127.0.0.1:8000")
print(request)
