from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from ...models import *
from django.contrib.auth import authenticate, login, logout

def login(request):
    
    return render(request, 'registration/login.html')

