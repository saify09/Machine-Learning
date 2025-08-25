from django.shortcuts import render

# Create your views here.
def index(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        operation = request.POST['operation']
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':            
            if num2!=0:
                result = num1 / num2 
            else:
                result="cannot divide by zero"
     
    return render(request, 'index.html', {'result': result})     