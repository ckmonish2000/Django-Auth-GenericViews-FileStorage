from django.shortcuts import render
from .models import testblog
# Create your views here.

def index(request):
    x=testblog.objects.get(id=1)
    context={"stuff":x}
    print(context)
    return render(request,"index.html",context)