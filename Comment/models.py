from django.db import models
from Usercenter.models import User

# Create your models here.

class Comment(models.Model):
    COMMENT_STATUS = (
        ('deleted','已删除'),
        ('active','正常'),
    )
    obj_type = models.CharField(max_length=10, verbose_name='评论对象')
    obj_id = models.IntegerField(null=True, verbose_name='评论对象ID')
    user_pk = models.ForeignKey(User, related_name='commented', verbose_name='被评论人')
    reply_user = models.ForeignKey(User, related_name='comments', verbose_name='我的评论')
    reply_content = models.TextField(verbose_name='评论内容')
    published = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    is_active = models.CharField(max_length=10, choices=COMMENT_STATUS, default='active', verbose_name='评论状态')
    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'