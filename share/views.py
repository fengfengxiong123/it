from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def test(request):
    ret=HttpResponse('<h1>123</h1>')
    print(ret)
    return ret