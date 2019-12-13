from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the StatsBoard index.")
def detail(request,user_name):
    return HttpResponse("You're looking at Player %s." % user_name)

def results(request, user_name):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % user_name)

def vote(request, user_name):
    return HttpResponse("You're voting on question %s." % user_name)