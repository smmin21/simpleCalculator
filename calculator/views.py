from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def result(request):
    input1 = int(request.GET['num1'])
    input2 = int(request.GET['num2'])
    usingoperator = request.GET['operator']

    if usingoperator == "sum":
        resultval = input1 + input2
    elif usingoperator == "sub":
        resultval = input1 - input2
    elif usingoperator == "mul":
        resultval = input1 * input2
    elif usingoperator == "div" and input2 == 0:
        resultval = "division by zero"
    else:
        resultval = input1 / input2
    
    return render(request, "result.html", {'result':resultval})
