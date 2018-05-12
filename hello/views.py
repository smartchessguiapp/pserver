from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

import process

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, 'db.html', {'greetings': greetings})

def startbot(request):
    print("starting bot")
    process.PopenProcess(["python","lichess-bot.py"],"lichess-bot")    
    return render(request, 'index.html')

def stopbot(request):
    print("stopping bot","not implemented")    
    return render(request, 'index.html')