from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.response import Response

from status.api.serializers import StatusInlineUserSerializer
from status.models import Status
from status.api.views import StatusAPIView

from .serializers import UserDetailSerializer


User = get_user_model()

class UserDetailApiView(generics.RetrieveAPIView):
    queryset 			= User.objects.filter(is_active = True)
    serializer_class 	= UserDetailSerializer
    lookup_field 		= 'username'

    def get_serializer_context(self):
        return {'request': self.request}


class UserStatusApiView(StatusAPIView):
    serializer_class 	    = StatusInlineUserSerializer

    def get_queryset(self, *args, **kwargs):
        username = self.kwargs.get('username', None)
        if username is None:
            return Status.objects.none()
        return Status.objects.filter(user__username = username)

    def post(sefl, request, *args, **kwargs):
        return Response({'detail': "Not allowed here!!"}, status = 400)

# class UserStatusApiView(generics.ListAPIView):
#     serializer_class 	    = StatusInlineUserSerializer
#     search_fields 			= ('user__username', 'content')
#     # pagination_class      = CFEPaginationAPIView

#     def get_queryset(self, *args, **kwargs):
#         username = self.kwargs.get('username', None)
#         if username is None:
#             return Status.objects.none()
#         return Status.objects.filter(user__username = username)