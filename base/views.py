from django.shortcuts import render

# Create your views here.

rooms = [
    {'id':1, "name":"Geo Politics"},
    {'id':2, "name":"Finance"},
    {'id':3, "name":"Real Estate"},
    {'id':4, "name":"Education"}
]

def home(request):
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None
    for r in rooms:
        if int(pk) == r['id']:
            room = r
            break
    context = {'room':room}
    return render(request, 'base/room.html', context)