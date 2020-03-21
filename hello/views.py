from django.shortcuts import render
import re
from datetime import datetime
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Big Django!")
def bill(request, wtf):
    content = "Hello, Bill, " + wtf
    return HttpResponse(content)

def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )