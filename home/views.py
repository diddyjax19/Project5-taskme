from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def home(request):
    now = datetime.datetime.now()
    time = now.strftime("%H:%M:%S")
    html = "<html><body>This is the taskit api page, Visited time: %s.</body></html>" % time
    return HttpResponse(html)