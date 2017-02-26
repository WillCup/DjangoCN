from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    auth_token = models.CharField(max_length=256, null=True, unique=True, verbose_name='Token码')
    email = models.EmailField(unique=True, verbose_name='邮箱')
    avatar = models.FilePathField(verbose_name='用户头像')
    mobile = models.CharField(max_length=12, unique=True, db_index=True, verbose_name='手机号')

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = '用户表'
