import re
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.urls import reverse
from pyparsing import Or
from .models import ChatRoom,Message
# Create your views here.
def lobby(request):
    return render(request, 'chat/lobby.html',{})


def listUsers(request):
    objs = User.objects.all().exclude(username = request.user)
    context = {
        'objs':objs
    }
    print(objs)
    return render(request,'chat/list.html',context)


def listChatrooms(request):
    objs = ChatRoom.objects.all()
    required_chatrooms = objs.filter(user1 = request.user) | objs.filter(user2 = request.user)
    context = {
        'objs':required_chatrooms
    }
    return render(request,'chat/chatrooms.html',context)

def getChatRoom(request,chatUuid):
    obj = ChatRoom.objects.get(chatUuid = chatUuid)
    if obj.user1 != request.user:
        recvr = obj.user1
    elif obj.user2 != request.user:
        recvr = obj.user2
    # chats = []
    chats = Message.objects.filter(chatRoom_id = chatUuid)
    print("chats: ",chats)
    context = {
        'obj':obj,
        'personobj' : recvr,
        'chats':chats
    }
    return render(request,'chat/chat.html',context)

def createChatRoom(request, pk, format=None):
    print("pk --> ",pk)

    user1_obj = User.objects.get(username = request.user) # current logged in user
    user2_obj = User.objects.get(pk = pk) #selected chat

    filtereddata = ChatRoom.objects.filter(user1=user1_obj) | ChatRoom.objects.filter(user1=user2_obj) | ChatRoom.objects.filter(user2=user1_obj) | ChatRoom.objects.filter(user2=user2_obj)
    # print("filtered data: ",filtereddata)
    check = (filtereddata.filter(user1 = user1_obj) & filtereddata.filter(user2 = user2_obj)) | filtereddata.filter(user1 = user2_obj) & filtereddata.filter(user2 = user1_obj)
    # print("check if chatroom exists for the 2 users : ",check)
    if len(check) == 0:
        chatroomcreated = ChatRoom.objects.create(
                    user1 = user1_obj,
                    user2 = user2_obj
                )
        print("uuid: "+chatroomcreated.chatUuid)
        print("New ChatRoom Created")
    # print(chatroom)
        # return redirect(reverse('chat:get_chatroom', kwargs={'chatUuid':chatroomcreated.chatUuid}))    
        
    return render(request,'chat/list.html',{})




    