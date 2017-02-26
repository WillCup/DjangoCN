from django.db import models
from django.utils import timezone
from usercenter.models import User


# Create your models here.

class Collect(models.Model):
    title = models.CharField(max_length=120, verbose_name='标题')
    link = models.CharField(max_length=250, null=True, verbose_name='项目链接')
    author = models.ForeignKey(User, null=True, related_name='projects', verbose_name='发布人')
    description = models.TextField(null=True, verbose_name='项目说明')
    pv = models.IntegerField(default=0, null=True, verbose_name='浏览量')
    comments = models.IntegerField(default=0, null=True, verbose_name='评论人数')
    published = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    created = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '项目'
        verbose_name_plural = '项目'
