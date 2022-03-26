from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def addition(request):
    number1 = int(request.GET['num1'])
    number2 = int(request.GET['num2'])
    res = number1 + number2
    return render(request,'maths.html',{'result':res})

def subtraction(request):
    number1 = int(request.GET['num1'])
    number2 = int(request.GET['num2'])
    res = number1 - number2
    return render(request,'maths.html',{'result':res})

def multiplication(request):
    number1 = int(request.GET['num1'])
    number2 = int(request.GET['num2'])
    res = number1 * number2
    return render(request,'maths.html',{'result':res})

def division(request):
    number1 = float(request.GET['num1'])
    number2 = float(request.GET['num2'])
    res = number1 / number2
    return render(request,'maths.html',{'result':res})

def remainder(request):
    number1 = float(request.GET['num1'])
    number2 = float(request.GET['num2'])
    res = number1 % number2
    return render(request,'maths.html',{'result':res})