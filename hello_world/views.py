#from django.http import HttpResponse
from django.shortcuts import render


'''def hello_page(request):
    return HttpResponse("Hello, World!")'''

def hello_page(request):
    return render(request, 'index.html')