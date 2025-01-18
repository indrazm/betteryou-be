from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework import status
from django.contrib.auth.models import User
from workspaces.models import Workspace, Space


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        print(request.data)

        if serializer.is_valid():
            # Remove password from validated_data since we'll handle it separately
            password = serializer.validated_data.pop("password")

            # Create user with create_user() for proper password hashing
            user = User.objects.create_user(
                password=password, **serializer.validated_data
            )

            # Create a workspace for the user
            suffix_random = str(user.id)
            workspace = Workspace.objects.create(
                name=f"{user.email}-{suffix_random}", user=user
            )

            Space.objects.create(name="default", workspace=workspace)

            response_data = {
                "message": "User registered successfully",
                "user": {
                    "id": user.id,
                    "email": user.email,
                },
            }

            return Response(response_data, status=status.HTTP_201_CREATED)

        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
