from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, Comment
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# 구현 남은것 : 웹 크롤링 (인기매물 긁어오기)

def home(request):
    return render(request, 'home.html')

@login_required(login_url='/login/')
def main(request):
    return render(request, 'main.html')

@login_required(login_url='/login/')
def report(request):
    rooms = Room.objects
    room_list = Room.objects.all()
    paginator = Paginator(room_list, 3)
    page = request.GET.get('page')
    pages = paginator.get_page(page)
    return render(request, 'report.html', {'rooms':rooms, 'pages':pages})

@login_required(login_url='/login/')
def detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    return render(request, 'detail.html', {'room':room})

def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method == 'POST':
        room = Room()
        room.author = request.user
        room.contractType = request.POST['contract']
        room.roomType = request.POST['room']
        room.content = request.POST['content']
        room.address1 = request.POST.get('address1', False);
        room.address2 = request.POST.get('address2', False);
        room.address3 = request.POST.get('address3', False);
        # room.address = request.POST['address']
        room.save()
        return redirect('detail', room.id)
    else:
        return render(request, 'new.html')

def update(request, pk):
    room = get_object_or_404(Room, pk=pk)
    
    if request.method == 'POST':
        room.author = request.user
        room.contractType = request.POST['contract']
        room.roomType = request.POST['room']
        room.content = request.POST['content']
        room.address1 = request.POST.get('address1', False);
        room.address2 = request.POST.get('address2', False);
        room.address3 = request.POST.get('address3', False);
        room.save()
        return redirect('detail', room.id)
    else:
        return render(request, 'update.html', {'room':room})

def delete(request, pk):
    room = get_object_or_404(Room, pk=pk)
    room.delete()
    return redirect('report')

def create_comment(request, pk):
    if request.method == "POST":
        comment = Comment()
        comment.author = request.user
        comment.content = request.POST['comment']
        comment.Room = Room.objects.get(pk=pk)
        comment.save()
        return redirect('detail', pk)

def delete_comment(request, room_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.author:
        comment.delete()
        return redirect('detail', room_pk)
    else:
        raise PermissionDenied

def search(request):
    address11 = request.POST.get('address1', False)
    address22 = request.POST.get('address2', False)
    rooms = Room.objects.filter(address1=address11, address2=address22)
    room_list = Room.objects.filter(address1=address11, address2=address22)
    paginator = Paginator(room_list, 3)
    page = request.GET.get('page')
    pages = paginator.get_page(page)
    return render(request, 'report.html', {'rooms':rooms, 'pages':pages, 'address1':address11, 'address2':address22})