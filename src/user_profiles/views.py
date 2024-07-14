from rest_framework import viewsets, permissions
from .models import UserProfile
from .serializers import UserProfileSerializer
from django_filters.rest_framework import DjangoFilterBackend


class IsAdminOrReadOnly(permissions.BasePermission):
    """Custom permission to only allow admins to edit it"""
    
    def has_permission(self, request, view):
        """Check if user is admin or read-only"""
        if view.action == "destroy":
            return request.user and request.user.is_staff
        return True


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['email', 'name', 'is_active']
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]

    def get_queryset(self):
        """Return objects for the current authenticated user only or all users for admin"""
        user = self.request.user
        if user.is_staff:
            return self.queryset
        return self.queryset.filter(id=user.id)

    def perform_create(self, serializer):
        """Create a new user profile"""
        serializer.save()

    def perform_update(self, serializer):
        """Update a user profile"""
        serializer.save()

    def perform_destroy(self, instance):
        """Delete a user profile"""
        instance.delete()


