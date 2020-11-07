from app.serializers import SkillsSerializer
from django.contrib.auth.models import User, Group
from django.db.models.query import QuerySet
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
        print(serializer.is_valid())
        serializer.is_valid(raise_exception=True)
        serializer.create(validated_data=request.data)
        # user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ListSkillsSet(viewsets.ModelViewSet):
    """
    Getting list of all skills
    """
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AddSkill(APIView):
    """
    Adding list of skill to this user profile
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        try:
            u = request.user.details
            skill = Skills.objects.filter(id__in=request.data["id"])
            u.skills.add(*skill)
            return Response({"status": "success"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({"status": "failed"}, status=status.HTTP_400_BAD_REQUEST)


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

