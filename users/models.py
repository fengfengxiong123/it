from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

from django.db import models


class MyUser(AbstractUser):
    name = models.CharField(u'中文名', max_length=12, blank=True, null=True)

    class Meta:
        verbose_name = u'用户详情'
        verbose_name_plural = u'用户详情'
