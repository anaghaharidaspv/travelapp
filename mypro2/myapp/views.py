from django.http import HttpResponse
from django.shortcuts import render
from .models import place, foot


# Create your views here.
def demo(request):
    obj=place.objects.all()
    obj1=foot.objects.all()
    return render(request, "index.html",{'result':obj,'res':obj1})


#def addition(request):
    #n1 = int(request.GET['num1'])
   # n2 = int(request.GET['num2'])
    #res1 = n1 + n2
   # res2=n1-n2
   # res3=n1*n2
    ##res4=n1/n2
    #return render(request, "result.html",{'result': res1,'subtr':res2,'multi':res3,'divi':res4})
