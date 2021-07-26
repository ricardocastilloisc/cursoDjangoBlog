from rest_framework.routers import DefaultRouter
from coments.api.views import CommentApiViewSet

router_coments = DefaultRouter()

router_coments.register(prefix='coments', basename='coments', viewset=CommentApiViewSet)