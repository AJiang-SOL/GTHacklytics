from django.shortcuts import render
from django.http import HttpResponse

def loadMain(request):
    return render(request,'Frontend/index.html')

def loadLogin(request):
    return render(request, 'Frontend/successfulLog.html')

def loadRegister(request):
    return render(request, 'Frontend/register.html')

def loadStats(request):
    #get objects from database
    return render(request, 'Frontend/statPage.html')
