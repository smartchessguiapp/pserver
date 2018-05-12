from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

import urllib3

#############################################

http = urllib3.PoolManager()

def get(url):
    r = http.request("GET", url)
    content = r.data.decode("utf-8")
    return content

#############################################

def index(request):    
    return render(request, 'report.html', {"content": "Welcome!"})

def startbot(request):
    print("starting bot")
    content = get("http://localhost:3000/b")
    return render(request, 'report.html', {"content": content})

def stopbot(request):
    print("starting bot")
    content = get("http://localhost:3000/s")
    return render(request, 'report.html', {"content": content})
