from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("hello,This is our first django project");
    return render(request,'index.html');

def about(request):
    return HttpResponse("hello , This is about page");

def contact(request):
    return HttpResponse("hello,This is contact page");