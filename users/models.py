from django.db import models
from django.contrib.auth.models import AbstractUser
from shortuuidfield import ShortUUIDField

# Create your models here.
# class User(AbstractUser):
#     userId = ShortUUIDField()


# class OnlineUser(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.username 