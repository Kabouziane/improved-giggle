from django.shortcuts import render, redirect
from .models import Message

def chat_room(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        content = request.POST.get('content')
        if username and content:
            Message.objects.create(username=username, content=content)
            return redirect('chat_room')

    messages = Message.objects.order_by('timestamp').all()
    return render(request, 'chat/room.html', {'messages': messages})
