from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def password(request):
    length=int(request.GET.get('length'))
    alpha='abcdefghijklmnopqrstuvwxyz'
    up=request.GET.get('upper')
    num=request.GET.get('number')
    spec=request.GET.get('specialchar')
    if up=='on':
        alpha+=alpha.upper()
    if num=='on':
        alpha+="1234567890"
    if spec=='on':
        alpha+=''.join(map(chr,range(33,48)))
    lstalpha=list(alpha)
    randlst=random.choices(lstalpha,k=length)
    randpass=''.join(map(str,randlst))
    return render(request,'generator/password.html',{'password':randpass})
def about(request):
    return render(request,'generator/about.html')
    