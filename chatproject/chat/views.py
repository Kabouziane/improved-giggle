from django.shortcuts import render, redirect
from .models import Message

def chat_room(request, room_name='general'):
    if request.method == 'POST':
        username = request.POST.get('username')
        content = request.POST.get('content')
        if username and content:
            Message.objects.create(username=username, content=content, room_name=room_name)
            return redirect('chat_room', room_name=room_name)

    messages = Message.objects.filter(room_name=room_name).order_by('timestamp')
    return render(request, 'chat/room.html', {
        'messages': messages,
        'room_name': room_name
    })
