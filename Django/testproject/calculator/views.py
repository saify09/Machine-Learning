from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request, methods=['GET', 'POST']):
    if request.method=="POST":
        num1=float(request.POST['num1'])
        num2=float(request.POST['num2'])
        operation=request.POST['operator']
        if operation=='+':
            result=num1+num2
        elif operation=='-':
            result=num1-num2
        elif operation=='*':
            result=num1*num2
        elif operation=='/':
            if num2!=0:
                result=num1/num2
            else:
                result="cannot divide by zero"
        return render(request,'calculator/index.html',{'result':result})
    
    return render(request,'calculator/index.html')