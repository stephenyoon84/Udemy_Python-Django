from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1><em>My Second App</em></h1>')

def help(request):
    helpdict = {
        'help_insert': "HELP PAGE"
    }
    return render(request, "app_two/help.html", context=helpdict)
