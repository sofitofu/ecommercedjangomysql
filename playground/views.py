from django.shortcuts import render
from django.http import HttpResponse

def say_hi(request):
    return render(request, 'hello.html')
