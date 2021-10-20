from django.shortcuts import render
from django.http import HttpResponse

# Create your views here; a view is a request handler
def sayHello(request):
    return render(request, 'hello.html',{'name':'Silvia'})