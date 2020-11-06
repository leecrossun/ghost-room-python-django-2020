from django.urls import path
from .views import chatbot, chatbot_unread, chatroom, create_room, delete_room, create_message, chat_refresh

urlpatterns = [
    path('chatbot/', chatbot, name="chatbot"),
    path('chatbot_unread/', chatbot_unread, name="chatbot_unread"),
    path('chatroom/<int:room_id>', chatroom, name="chatroom"),
    path('create_room/', create_room, name="create_room"),
    path('delete_room/<int:room_id>', delete_room, name="delete_room"),
    path('create_message/<int:room_id>', create_message, name="create_message"),
    path('chat_refresh/<int:room_id>', chat_refresh, name="chat_refresh"),
]