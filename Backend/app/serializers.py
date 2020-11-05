from django.contrib.auth.models import User, Group
from django.db.models import fields
from rest_framework import serializers
from .models import UserDetail, Skills


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class SkillsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skills
        fields = ['name', 'level']


class UserDetailSerializer(serializers.HyperlinkedModelSerializer):
    skills = SkillsSerializer(many=True, read_only=True)

    class Meta:
        model = UserDetail
        fields = ['mobile_num', 'college_name', 'skills']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    details = UserDetailSerializer()

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'details']
