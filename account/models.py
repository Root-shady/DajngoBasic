from django.db import models
# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, username,
                is_staff, is_admin, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
            is_staff=is_staff, is_active=True,
            is_admin=is_admin,
            joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password=None, **extra_fields):
        return self._create_user(email, password, True, False,
            **extra_fields)

    def create_superuser(self, email, password, username, **extra_fields):
        return self._create_user(email, password, username, False, True,
            **extra_fields)

    def get_by_natural_key(self, username):
        return self.get(email__iexact=username)

class User(AbstractBaseUser,  PermissionsMixin):
    """
    Custom user class
    """
    username = models.CharField(max_length=30,verbose_name="用户名", unique=True)
    email = models.CharField(max_length=100, unique=True, db_index=True,verbose_name="邮箱")
    real_name = models.CharField(max_length=100, null=True, verbose_name='用户真实名称')
    joined = models.DateTimeField(auto_now_add=True,verbose_name="加入时间")
    is_active = models.BooleanField(default=True, verbose_name="账户可用")
    is_staff = models.BooleanField(default=False, verbose_name="公司成员")
    is_admin = models.BooleanField(default=False,verbose_name="超级管理员")
    is_sub = models.BooleanField(default=False, verbose_name="子委托方")

    USERNAME_FIELD = 'username'
    objects = CustomUserManager()
    # 这里会影响到createsuperuser的创建
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name_plural = "系统用户"

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username

    def clean(self):
        """
        If password's length is less than 6 character, it is now allowed
        """
        if len(self.email) < 2:
            raise ValidationError(_("邮件不为空"))


    def save(self, *args, **kwargs):
        if not self.pk:
            self.set_password(self.password)
        self.username = self.username.strip()
        super(User, self).save(*args, **kwargs)
