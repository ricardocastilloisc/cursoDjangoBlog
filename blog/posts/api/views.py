from posts.api.permissions import IsAdminOrReadOnly
from rest_framework.viewsets import ModelViewSet
from posts.models import Post
from posts.api.serializers import PostSerializer
from django_filters.rest_framework import DjangoFilterBackend


class PostApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category','category__slug']
    #filterset_fields = ['category']
