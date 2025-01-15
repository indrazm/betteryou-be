from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework import status
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from workspaces.models import Workspace, Space

User = get_user_model()


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            password = serializer.validated_data.get("password")
            user = serializer.save(password=make_password(password))

            # Create a workspace for the user
            workspace = Workspace.objects.create(name=f"{user.email}", user=user)
            workspace.save()

            # Create a space for the user
            space = Space.objects.create(name="default", workspace=workspace)
            space.save()

            response_data = {
                "message": "User registered successfully",
                "user": {
                    "id": user.id,
                    "email": user.email,
                },
            }

            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
