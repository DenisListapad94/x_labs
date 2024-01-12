from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ..serializers import RegisterUserSerializer


class RegisterUserApiView(APIView):
    serializer_class = RegisterUserSerializer
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        return Response(
            data=user_data,
            status=status.HTTP_201_CREATED
     )
