from rest_framework import serializers

from apps.posts.models import Post
from apps.users.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)


    class Meta:
        model = Post
        fields = (
            "id",
            "user",
            "title",
            "content",
            "created_at",
        )
        extra_kwargs = {
            "posted_on": {
                "read_only": True,
            }
        }