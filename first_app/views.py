from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    # d=['a', 'b', 'c']
    # d= datetime.datetime.now()
    # d=10
    # d=['Jane', 'Janet', 'Joe']
    d= ['Banana', 'Mango', 'Orange']
    # d=['<b>I</b> <button>love</button> <span>dogs</span>']
    return render(request,'test.html',{'d':d})