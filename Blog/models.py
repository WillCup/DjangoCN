from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from Usercenter.models import User

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class BlogPost(models.Model):
    STATUS_CHOICES = (
        ('draft', '草稿'),
        ('published', '发表')
        )
    title = models.CharField(max_length=250, verbose_name='标题')
    slug = models.SlugField(max_length=250, unique_for_date='publish', verbose_name='短标签')
    author = models.ForeignKey(User, related_name='blog_posts', verbose_name='作者')
    body = models.TextField(verbose_name='内容')
    comments = models.IntegerField(default=0, verbose_name='评论数')
    publish = models.DateTimeField(default=timezone.now, verbose_name='发布日期')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新日期')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name='状态')

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def get_absolute_url(self):
        return reverse('Blog:post_detail',
            args=[self.publish.year,
            self.publish.strftime('%m'),
            self.publish.strftime('%d'),
            self.slug])

    def __str__(self):
        return self.title