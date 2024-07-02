from django.shortcuts import render, HttpResponse

# Create your views here.


def indexPage(request):
    return HttpResponse("Hello, This is my web page")


def aboutUS(request):
    return HttpResponse("เกี่ยวกับฉัน")


def contactUs(request):
    return HttpResponse("ติดต่อฉัน")
