from django.shortcuts import render, redirect, get_object_or_404
from .models import Message, Room
from .forms import MessageForm, RoomForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
import json
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required(login_url='/login/')
def chatbot(request):
    if request.user.username == "hyosun":
        all_room = Room.objects.all()
    else:
        all_room = Room.objects.filter(user=request.user)
    return render(request, 'chatbot.html', {'all_room':all_room})

@login_required(login_url='/login/')
def chatbot_unread(request):
    if request.user.username == "hyosun":
        all_room = Room.objects.filter(admin_read=False)
    else:
        all_room = Room.objects.filter(user=request.user, user_read=False)
    return render(request, 'chatbot.html', {'all_room':all_room})

@login_required(login_url='/login/')
def chatroom(request, room_id):
    my_room = get_object_or_404(Room, pk=room_id)
    if request.user.username == "hyosun":
        my_room.admin_read = True
    else:
        my_room.user_read = True
    my_room.save()
    message_form = MessageForm()
    return render(request, 'chatroom.html', {'my_room':my_room, 'message_form': message_form})

def create_room(request):
    my_room = RoomForm().save(commit=False)
    my_room.user = request.user.username
    my_room.admin_read = False
    my_room.user_read = False
    my_room.save()
    return redirect('chatroom', my_room.id)

def delete_room(request, room_id):
    my_room = get_object_or_404(Room, pk=room_id)
    my_room.delete()
    return redirect('chatbot')  


def create_message(request, room_id):
    message_form = MessageForm(request.POST)

    if message_form.is_valid():
        tmp_form = message_form.save(commit=False)
        tmp_form.sender = request.user.username
        tmp_form.room = Room.objects.get(pk=room_id)
        tmp_form.save()

        my_room = get_object_or_404(Room, pk=room_id)
        my_room.last_message = tmp_form.body
        if request.user.username == "hyosun":
            my_room.user_read = False
        else:
            my_room.admin_read = False
        my_room.save()
        return redirect('chatroom', room_id)


def chat_refresh(reqeust, room_id):
    room = get_object_or_404(Room, pk=room_id)
    if reqeust.user.username == "hyosun":
        room.admin_read = True
    else:
        room.user_read = True
    room.save()

    messages = Message.objects.filter(room = room_id)
    i = 0
    message_items = {}
    for message in  messages:
        message_items['item'+str(i)] = '{"sender": "' + message.sender + '", "body": "' + message.body + '"}'
        i += 1

    return HttpResponse(json.dumps(message_items), content_type="application/json")
