from django.db import models


class UserInfoManager(models.Manager):
    def create(self, name, password):
        user = UserInfo()
        user.uname = name
        user.upwd = password
        return user
# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=10)
    upwd = models.CharField(max_length=10)

    class Meta:
        db_table = 'userinfo'
    userObject = UserInfoManager()
    def __str__(self):
        return self.uname.encode('utf-8')


