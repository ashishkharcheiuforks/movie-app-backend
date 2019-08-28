from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializers import UserSerializer


class CurrentUserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'user': serializer.data})
