from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework import permissions

from apps.profiles.serializers import ProfileSerializer


User = get_user_model()


class ProfileView(generics.CreateAPIView):

    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        serializer.save(ip_address=self.request.META["REMOTE_ADDR"])