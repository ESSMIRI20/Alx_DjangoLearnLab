from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .models import CustomUser  # Make sure you're importing the correct custom user model
from .serializers import RegisterSerializer

# RegisterView remains as is
class RegisterView(generics.GenericAPIView):
    """
    View to handle user registration.
    """
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Follow User view using generics.GenericAPIView for more flexibility
class FollowUserView(generics.GenericAPIView):
    """
    View to follow a user.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = CustomUser.objects.get(id=user_id)  # Use CustomUser here instead of User
        except CustomUser.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        if user_to_follow == request.user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(user_to_follow)
        return Response({"detail": "Successfully followed."}, status=status.HTTP_200_OK)

# Unfollow User view using generics.GenericAPIView
class UnfollowUserView(generics.GenericAPIView):
    """
    View to unfollow a user.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_unfollow = CustomUser.objects.get(id=user_id)  # Use CustomUser here instead of User
        except CustomUser.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        if user_to_unfollow == request.user:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.remove(user_to_unfollow)
        return Response({"detail": "Successfully unfollowed."}, status=status.HTTP_200_OK)

users = CustomUser.objects.all()