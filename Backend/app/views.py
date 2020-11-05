from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from app.models import Skills, UserDetail
from rest_framework import permissions
from app.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


# class AccountViewSet(viewsets.ModelViewSet):
#     """
#     A simple ViewSet for viewing and editing accounts.
#     """
#     queryset = Account.objects.all()
#     serializer_class = AccountSerializer
#     permission_classes = [IsAccountAdminOrReadOnly]
