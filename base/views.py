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
    return render(request, 'home.html', context)

def room(request):
    return render(request, 'room.html')