from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
#from rest_framework.decorators import action

from apps.posts.models import Post
from apps.posts.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
