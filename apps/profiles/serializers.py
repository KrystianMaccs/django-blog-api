from rest_framework import serializers

from django.contrib.auth import get_user_model

from apps.users.tasks import enrich_user

from apps.profiles.models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile

    def create(self, validated_data):
        profile = Profile.objects.create_user(
            ip_address=validated_data["ip_address"],
        )
        enrich_user.delay(profile.pk)

        return profile