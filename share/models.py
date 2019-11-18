from django.db import models
from mdeditor.fields import MDTextField
# from django.contrib.auth.models import User
from users.models import User
from it import settings

# Create your models here.
class Dot(models.Model):
    question = models.CharField(verbose_name='问题', max_length=200, blank=True, null=True)
    answer = MDTextField(verbose_name='答案', max_length=10000, blank=True, null=True)
    summary = models.CharField(verbose_name='摘要', max_length=200, blank=True, null=True)
    font = models.BooleanField(verbose_name='前端', default=True)
    backend= models.BooleanField(verbose_name='后端', default=True)
    server = models.BooleanField(verbose_name='服务器', default=True)
    dev = models.BooleanField(verbose_name='开发', default=True)
    product = models.BooleanField(verbose_name='部署', default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='用户', null=True, )
    date_time_last = models.DateTimeField(verbose_name='修改时间', auto_now=True, blank=True, null=True, )
    date_time_first = models.DateTimeField(verbose_name='创建时间', auto_now_add=True, blank=True, null=True, )
