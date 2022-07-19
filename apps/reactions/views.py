from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.reactions.models import Like, UnLike
from apps.reactions.serializers import LikeSerializer, UnLikeSerializer


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True)
    def like(self, request, pk):
        post = self.get_object()
        post.likes.add(request.user)

        return Response(status=status.HTTP_200_OK)


class UnLikeViewSet(viewsets.ModelViewSet):
    queryset = UnLike.objects.all()
    serializer_class = UnLikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True)
    def unlike(self, request, pk):
        post = self.get_object()
        post.likes.remove(request.user)

        return Response(status=status.HTTP_200_OK)