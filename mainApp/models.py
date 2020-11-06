from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    contractType = models.CharField(max_length=50)
    roomType = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    address1 = models.TextField()
    address2 = models.TextField(default='')
    address3 = models.TextField(default='')
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    Room = models.ForeignKey(Room, on_delete=models.CASCADE)
