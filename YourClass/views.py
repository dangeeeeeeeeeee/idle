from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<center><h3>YourClass</h3></center>")

from django.template import loader

def index(request):
    #return HttpResponse("<center><h3>안녕 장고^^</h3></center>")
    template = loader.get_template('index.html')
    #return HttpResponse(template.render()) #나중에 session변수값을 가져오지 못함
    return HttpResponse(template.render({}, request)) #반드시.. ruquest를 받아야 좋음 
