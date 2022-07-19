from rest_framework import serializers

from apps.reactions.models import Like, UnLike
from apps.users.serializers import UserSerializer


class LikeSerializer(serializers.ModelSerializer):

    #user = UserSerializer(read_only=True)

    likes = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Like
        fields = (
            "id",
            "user",
            "title",
            "content",
            "posted_on",
            "likes",
        )
        extra_kwargs = {
            "posted_on": {
                "read_only": True,
            }
        }


class UnLikeSerializer(serializers.ModelSerializer):

    # = UserSerializer(read_only=True)

    un_likes = UserSerializer(read_only=True, many=True)

    class Meta:
        model = UnLike
        fields = (
            "id",
            "user",
            "title",
            "content",
            "posted_on",
            "un_likes",
        )
        extra_kwargs = {
            "posted_on": {
                "read_only": True,
            }
        }