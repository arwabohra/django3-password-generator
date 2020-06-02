from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request,'generator/home.html')

def password(request):

    characters=list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('FGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    if request.GET.get('Special'):
        characters.extend(list('!@#$%^&*()'))

    thepassword=''

    length=int(request.GET.get('length'))

    for i in range(length):
        thepassword+=random.choice(characters)

    return render(request,'generator/password.html',{'password':thepassword})

def aboutus(request):
    return render(request, 'generator/AboutUs.html')





