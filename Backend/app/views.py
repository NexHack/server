from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.routers import flatten
from app.models import Skills, UserDetail
from rest_framework import permissions
from app.serializers import UserSerializer, GroupSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


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
        # uniq = list(set(li))
        # for i in uniq:
        #     if(request.user.id==li['user__id']):

        return Response(li)
