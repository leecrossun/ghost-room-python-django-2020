from django.db import models

# Create your models here.
class Room(models.Model):
    user = models.CharField(max_length=30, null=True) #여기도 user fk로 바꿔야 함
    user_read = models.BooleanField()
    admin_read = models.BooleanField()
    last_message = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.user
        
    def summary(self):
        return self.last_message[:40]


class Message(models.Model):
    time = models.DateTimeField(auto_now=True)
    sender = models.CharField(max_length=30) #여기도 user fk로 바꿔야 함
    body = models.CharField(max_length=1000)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.body
