from django.db import models

class Message(models.Model):
    username = models.CharField(max_length=255)
    content = models.TextField()
    room_name = models.CharField(max_length=255, default='general')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.username}: {self.content}'

    class Meta:
        ordering = ['timestamp']
