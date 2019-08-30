from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializers import UserSerializer, UserCreationSerializer


class CurrentUserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'user': serializer.data})


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreationSerializer
    permission_classes = (permissions.AllowAny,)
