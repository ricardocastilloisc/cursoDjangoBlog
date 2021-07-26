from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter

from coments.models import Comment
from coments.api.serializers import CommentSerializer

class CommentApiViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = [OrderingFilter]
    ordering = ['-created_at']

