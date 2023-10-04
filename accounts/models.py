from django.db import models
# Django 가 사용하는 default User 모델 기반으로 개발 할거다.
# 그래서 상속을 받음
from django.contrib.auth.models import AbstractUser

# Create your models here.
# 사용하고 싶으면, AUTH_USER_MODEL = 'accounts.User'이거 써야함.
# 최대한 user만들어 놓고 migrate해야한다! 

class User(AbstractUser):
    pass