from channels.generic.websocket import AsyncWebsocketConsumer
import json
class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_group_name = self.scope['url_route']['kwargs']['room_name']
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
        print('Disconnected')

    async def receive(self, text_data): #used for sending SDP to peer
        receive_dict = json.loads(text_data)
        action = receive_dict['action']
        if action == 'new-offer' or action =='new-answer':
            receiver_channel_name = receive_dict['message']['receiver_channel_name']
            receive_dict['message']['receiver_channel_name']= self.channel_name

            await self.channel_layer.send(
                receiver_channel_name, 
                    {
                        'type':'send_sdp', #with the help of this function
                        'receive_dict': receive_dict, #the message
                    }
            )
            return
        receive_dict['message']['receiver_channel_name'] = self.channel_name #channel name of current user

        await self.channel_layer.group_send(#helps to broadcast the message to the whole group
            self.room_group_name, #this id the group where message is to be broadcasted
            {
                'type':'send_sdp', #with the help of this function
                'receive_dict': receive_dict, #the message
            }
        )

    async def send_sdp(self, event):
        receive_dict = event['receive_dict']

        await self.send(text_data= json.dumps( #send message into the group (to be read in the front end)
           receive_dict
        ))
