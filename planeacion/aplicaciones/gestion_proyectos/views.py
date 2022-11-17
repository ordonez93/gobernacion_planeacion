from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def inicio(request):
    fecha_now = datetime.datetime.now()
    return render(request, 'layout.html', {"fecha": fecha_now.year})