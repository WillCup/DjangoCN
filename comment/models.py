from django.db import models
from usercenter.models import User
from blog.models import BlogPost
from collect.models import Collect
from faquestion.models import FAQuestion


class BlogPostManager(models.Manager):
    def get_queryset(self):
        return super(BlogPostManager, self).get_queryset().filter(obj_type='blog')


class UserManager(models.Manager):
    def get_queryset(self):
        return super(UserManager, self).get_queryset().filter(obj_type='user')


class CollectManager(models.Manager):
    def get_queryset(self):
        return super(CollectManager, self).get_queryset().filter(obj_type='collect')


class FAQuestionManager(models.Manager):
    def get_queryset(self):
        return super(FAQuestionManager, self).get_queryset().filter(obj_type='question')


class Comment(models.Model):
    """
    dynamic create record for objs.  Just for design.
    """
    STATUS_CHOICES = (
        ('deleted', '已删除'),
        ('active', '正常'),
    )
    OBJ_CHOICES = (
        ('user', User),
        ('blog', BlogPost),
        ('collect', Collect),
        ('question', FAQuestion)
    )
    obj_type = models.CharField(max_length=10, choices=OBJ_CHOICES, default='blog', verbose_name='评论对象')
    obj_id = models.IntegerField(null=True, verbose_name='评论对象ID')  # need recode.
    user_pk = models.ForeignKey(User, related_name='commented', verbose_name='被评论人')
    reply_user = models.ForeignKey(User, related_name='comments', verbose_name='我的评论')
    reply_content = models.TextField(verbose_name='评论内容')
    published = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    is_active = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active', verbose_name='评论状态')

    objects = models.Manager()
    # set custom Manager
    user = UserManager()
    blog = BlogPostManager()
    collect = CollectManager()
    question = FAQuestionManager()

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'
