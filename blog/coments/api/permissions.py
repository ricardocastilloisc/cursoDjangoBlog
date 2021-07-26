from rest_framework.permissions import BasePermission
from coments.models import Comment

class IsOwnerOrReadAndCreateOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'POST':
            return True
        else:
            id_coment = view.kwargs['pk']
            coment = Comment.objects.get(pk=id_coment)
            id_user = request.user.pk
            id_user_coment = coment.user_id

            if id_user_coment == id_user:
                return True
            return False
