import json

from channels.generic.websocket import AsyncWebsocketConsumer


class PhotoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            'photos',
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            'photos',
            self.channel_name
        )

    async def receive(self, text_data):
        await self.channel_layer.group_send(
            'photos',
            {
                'type': 'event',
            }
        )

    async def event(self, event):
        await self.send(
            text_data=json.dumps({
                'message': 'updated',
            })
        )
