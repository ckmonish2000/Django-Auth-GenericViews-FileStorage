from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .form import fileform
# Create your views here.


class tes(View):
    def get(self,request):
        context={"stuff":fileform()}
        return render(request,"index.htm",context)
    
    def post(self,request):
        if(request.method=='POST'):
            a=handle(request.FILES['file'])
            print(a)
            return HttpResponse("uploaded")
        else:
            context={"stuff":fileform()}
            return render(request,"index.htm",context)



def handle(f):
    
    with open('t/media/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  
    x=f't/media/{f.name}'
    return x
    
