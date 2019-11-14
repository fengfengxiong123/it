from django.db import models
from mdeditor.fields import MDTextField


# Create your models here.
class Dot(models.Model):
    question = models.CharField(u'问题', max_length=200, blank=True, null=True)
    answer = MDTextField(u'答案', max_length=10000, blank=True, null=True)
