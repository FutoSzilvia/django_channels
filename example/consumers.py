import json
from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http


# from asgiref.sync import async_to_sync
# group exists only in channels 1 (ebbe menne, de majd ha a masikkal ossze kell tenni akkor jobb a channels 3)
# django 1 kell hozza, mashoz django 3 --- six package miatt, bar azt pip insall six 1 -el meg lehet oldani


@channel_session_user_from_http
def ws_connect(message):
    Group('users').add(message.reply_channel)
    Group('users').send({
        'text': json.dumps({
            'username': message.user.username,
            'is_logged_in': True
        })
    })


@channel_session_user
def ws_disconnect(message):
    Group('users').send({
        'text': json.dumps({
            'username': message.user.username,
            'is_logged_in': False
        })
    })
    Group('users').discard(message.reply_channel)

# def connect(self):
#     async_to_sync(self.channel_layer.group_add)("chat", self.channel_name)
#
#
# def disconnect(self, close_code):
#     async_to_sync(self.channel_layer.group_discard)("chat", self.channel_name)
#
#
# def receive(self, text_data):
#     async_to_sync(self.channel_layer.group_send)(
#         "chat",
#         {
#             "type": "chat.message",
#             "text": text_data,
#         }
#     )
#
#
# def chat_message(self, event):
#     self.send(text_data=event["text"])
