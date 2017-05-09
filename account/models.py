from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone


class User(models.Model):
    """
    Custom user class
    """
    user = models.OneToOneField(User, related_name='usermodel')
    real_name = models.CharField(max_length=100, null=True, verbose_name='用户真实名称')

    class Meta:
        verbose_name_plural = "系统用户"

    def __str__(self):
        return self.username
