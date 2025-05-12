from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def second_view(request):
    return render(request, 'second.html')

def third_view(request):
    return render(request, 'second.html')