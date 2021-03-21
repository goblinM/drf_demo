from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Ariticles(models.Model):
    article_id = models.IntegerField(verbose_name='文章id', unique=True)
    title = models.CharField(verbose_name=u'文章题目', max_length=124, default='')
    author = models.CharField(verbose_name=u'文章作者', max_length=64, default='')
    public_date = models.CharField(verbose_name=u'文章发版日期', max_length=124)
    describe = models.CharField(verbose_name='文章简介', max_length=1024)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u"文章表"
        verbose_name_plural = verbose_name
        db_table = u"articles"


class Authors(models.Model):
    author_id = models.IntegerField(verbose_name='作者id', unique=True)
    name = models.CharField(verbose_name=u'作者名', max_length=64)
    age = models.IntegerField(verbose_name='作者年龄', default=0)
    address = models.CharField(verbose_name='作者居住地址', max_length=2056, default='')

    class Meta:
        verbose_name = u'作者表'
        verbose_name_plural = verbose_name
        db_table = u'authors'
