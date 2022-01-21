from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.status import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from watchlist_app.api import serializers
from watchlist_app import models


class StreamPlatformTestCase(APITestCase):
    
    def setUp(self):
        pass # To be re-continued... After return

    def test_streamplatform_create(self):
        data = {
            "name":"NetFlix",
            "about":"#1 Streaming Platform",
            "website":"https://www.netflix.com"
        }
        response = self.client.post(reverse('streamplatform-list'), data)
        self.assertEqual(response.status_code, HTTP_200_OK)