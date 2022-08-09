import json 
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from .models import ChatRoom,Message
from django.contrib.auth.models import User
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['path_remaining'].replace('/', '')
        print(self.room_name)
        self.room_group_name = 'chat_%s' % self.room_name
        # self.room_group_name = 'test'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        self.user_id = self.scope['user'].id
        #Find the room object
        room = await database_sync_to_async(ChatRoom.objects.get)(chatUuid = self.room_name)
        #create new chat object
        chat = Message(
           chatRoom = room,
           sender = self.scope['user'],
           message=message,
        )
        await database_sync_to_async(chat.save)()

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message', #name of the function that handles this event
                'message':message,
                'user_id':self.user_id,
            }
        )

    async def chat_message(self,event):#handling event ,using event to retreive the message
        message = event['message']
        user_id = event['user_id']
        await self.send(text_data = json.dumps({
            'type':'chat',
            'message':message,
            'user_id':user_id,
        }))