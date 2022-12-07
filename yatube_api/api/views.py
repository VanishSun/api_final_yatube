from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .serializers import CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer
from posts.models import (
    Follow,
    Group,
    Post
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


# class FollowViewSet(viewsets.ModelViewSet):
#     serializer_class = FollowSerializer

#     def get_queryset(self):
#         return super().get_queryset()