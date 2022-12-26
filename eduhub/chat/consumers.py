# chat/consumers.py
import json
from asgiref.sync import async_to_sync, sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils import timezone
from .models import Message
from courses.models import Course
from django.contrib.auth.models import User


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.id = self.scope['url_route']['kwargs']['course_id']
        self.room_group_name = f'chat_{self.id}'
        # join room group
        await self.channel_layer.group_add(
        self.room_group_name,
        self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
            )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json['username']
        course_id = text_data_json['course_id']
        await self.save_message(username, course_id, message)

        # send message to room group
        await self.channel_layer.group_send(
        self.room_group_name,
        {
        'type': 'chat_message',
        'message': message,
        'username':username,
        'course_id':course_id,
        'datetime': timezone.now().isoformat(),
        }
        )

    # receive message from room group
    async def chat_message(self, event):
        # send message to WebSocket
        await self.send(text_data=json.dumps(event))

    @sync_to_async
    def save_message(self, username, course_id, message):
        course = Course.objects.get(id=course_id)
        user = User.objects.get(username=username)
        Message.objects.create(user=user, course=course, message=message)

