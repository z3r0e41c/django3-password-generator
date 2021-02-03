from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request,'generator/home.html')

def about(request):
    return render(request,'generator/about.html')

def password(request):

    characeters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characeters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characeters.extend(list('0123456789'))
    if request.GET.get('special'):
        characeters.extend(list('!@#$%^&*'))

    length = int(request.GET.get('length',12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characeters)



    return render(request,'generator/password.html', {'password':thepassword})
