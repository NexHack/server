from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import validate_comma_separated_integer_list
from django.forms.fields import DateTimeField


class Skills(models.Model):
    name = models.CharField(max_length=100, blank=False,
                            null=False, default="Python")
    level = models.SmallIntegerField()


class UserDetail(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="details")
    skills = models.ManyToManyField(Skills, related_name='skills')
    college_name = models.CharField(max_length=100)
    mobile_num = models.CharField(max_length=10)
