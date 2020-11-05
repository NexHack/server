from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.routers import flatten
from app.models import Skills, UserDetail
from rest_framework import permissions
from app.serializers import UserSerializer, GroupSerializer, RegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class RegisterApi(APIView):
    """
    Api for registering the user
    """

    def post(self, request):
        print("here")
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserViewSet(viewsets.ModelViewSet):
    """
    View User Data and Allow Change if it is his own data
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class GetSuggestedUsers(APIView):
    """
    Get All Users with all the skills as that of this user
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        det = request.user.details
        skills = det.skills.prefetch_related('skills').all()
        li = []
        for x in skills:
            # All users with this skill
            z = x.skills.values('user__id', 'user__username')
            z = list(z)
            li.append({x.name: z})
        print(li)
        return Response(li)
