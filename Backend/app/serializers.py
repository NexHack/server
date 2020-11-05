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


class RegisterSerializer(serializers.ModelSerializer):
    user_detail = UserDetailSerializer(required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password',
                  'first_name', 'last_name', 'user_detail')

    def create(self, validated_data):
        print("Coming to create")
        user_data = validated_data.pop('user_detail')
        user = User.objects.create(
            username=validated_data.pop('username'), password=validated_data.pop('password'))
        d1 = UserDetailSerializer(user_data)

        UserDetail.objects.create(
            user=user, mobile_num=d1["mobile_num"], college_name=d1["college_name"])
