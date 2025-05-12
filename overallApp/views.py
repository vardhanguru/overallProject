from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first_view(request):
    data = {'name':'vardhan',
            'fruits':['apple','grapes'],
            'logged_in':True}


    return render(request, 'base.html', context=data)

def login_view(request):
    return render(request, 'login.html')