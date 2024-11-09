from django.shortcuts import render,redirect
from .models import Room,Message

# Create your views here.
def Home(request):
    if request.method == "POST":
        username = request.POST["username"]
        room = request.POST["room"]
        
        existing_room = Room.objects.get_or_create(room_name=room)
        
        return redirect("room", room_name=room, username=username)
    
    return render(request,'home.html')

def Rooms(request,room_name,username):
    
    existing_room = Room.objects.get(room_name=room_name)
    messages = Message.objects.filter(room=existing_room)
    
    
    return render(request,'room.html',{'room':room_name,'user':username,'messages':messages})