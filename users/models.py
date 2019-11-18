from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

from django.db import models


class User(AbstractUser):
    nickname = models.CharField(verbose_name='昵称', max_length=12, unique=True)

    # 必须有一个唯一标识--USERNAME_FIELD
    # USERNAME_FIELD = 'nickname'

    # 创建账户时必须的字段
    # REQUIRED_FIELDS = ['username','password']
