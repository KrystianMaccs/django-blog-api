from ipaddress import ip_address
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from apps.profiles.models import Profile
from apps.profiles.factories import ProfileFactory

User = get_user_model()

class ProfileTest(APITestCase):
    def test_get_profile(self):
        data = {
            "ip_address": "54.182.0.19",
            "country_code": "US",
            "country_geoname_id": "US",
            "joined_on_holiday": False
        }
        response = self.client.post(reverse('signup'), data=data, REMOTE_ADDR='54.182.0.19')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        profile = Profile.objects.first()
        self.assertEqual(profile.joined_on_holiday, data["joined_on_holiday"])
        self.assertEqual(profile.ip_address, '54.182.0.19')
        self.assertEqual(profile.country_code, 'US')
        
    def test_get_profile_joined_on_holiday(self):
        ip_address = '54.182.0.19'
        joined_on_holiday = False
        profile = ProfileFactory(ip_address='54.182.0.19', joined_on_holiday=False)
        #response = self.client.post(reverse(), data=)
        #self.assertEqual(response.status_code, status.HTTP_200_OK)
