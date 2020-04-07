from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from mode.models import testblog
# Create your views here.


def users(request):
    obj=testblog.objects.all()
    lst=[]
    for x in obj:
        lst.append({"title":x.title,"body":x.body})
    return JsonResponse({"list":lst})
