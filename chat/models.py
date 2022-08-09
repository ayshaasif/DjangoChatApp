from django.db import models
from django.dispatch import receiver
from shortuuidfield import ShortUUIDField
# from users.models import User
from django.contrib.auth.models import User
# Create your models here.
2

class ChatRoom(models.Model):
    chatUuid = ShortUUIDField(primary_key = True)
    # chatRoomName = models.CharField(max_length=225)
    user1 = models.ForeignKey(User,null=True,default=None,related_name='user1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User,null=True,default=None, related_name='user2', on_delete=models.CASCADE)

    def __str__(self):
        # return str(self.user1.username)+" and "+str(self.user2.username)
        return str(self.chatUuid)

class Message(models.Model):
    time = models.DateTimeField(auto_now=True)
    chatRoom =  models.ForeignKey('ChatRoom', on_delete=models.CASCADE)
    sender = models.ForeignKey(User,null=True,default=None, on_delete=models.CASCADE)
    message = models.CharField(max_length=225)

