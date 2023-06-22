from rest_framework import viewsets, permissions, generics, mixins
from .serializers import CustomerSerializer, CustomerProfileSerializer, AddressSerializer
from django.contrib.auth import get_user_model
from .models import CustomerProfile
from . import permissions as my_permissions

User = get_user_model()


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.AllowAny]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class ProfileList(generics.ListAPIView):
    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProfileViewSets(viewsets.ModelViewSet):
    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerProfileSerializer
    permission_classes = [my_permissions.IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return CustomerProfile.objects.filter(user=self.request.user)
