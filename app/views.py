from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':20,'b':30,'c':10}
    return render(request,'condition.html',d)
    