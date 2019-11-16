from django.db import models
from mdeditor.fields import MDTextField
from django.contrib.auth.models import User


# Create your models here.
class Dot(models.Model):
    question = models.CharField(verbose_name='问题', max_length=200, blank=True, null=True)
    answer = MDTextField(verbose_name='答案', max_length=10000, blank=True, null=True)
    summary = models.CharField(verbose_name='摘要', max_length=200, blank=True, null=True)
    choices = (('font', '前端'), ('back', '后端'), ('server', '服务器'), ('dev', '开发'), ('product', '部署'))
    labelone = models.CharField(verbose_name='标签一', max_length=10, choices=choices, blank=True, null=True, default='font')
    labeltwo = models.CharField(verbose_name='标签二', max_length=10, choices=choices, blank=True, null=True, default='font')
    labelthree = models.CharField(verbose_name='标签三', max_length=10, choices=choices, blank=True, null=True, default='font')
    labelfour = models.CharField(verbose_name='标签四', max_length=10, choices=choices, blank=True, null=True, default='font')
    labelfive = models.CharField(verbose_name='标签五', max_length=10, choices=choices, blank=True, null=True, default='font')
    user = models.ForeignKey(User, on_delete=models.SET_NULL,verbose_name='用户',null=True)
