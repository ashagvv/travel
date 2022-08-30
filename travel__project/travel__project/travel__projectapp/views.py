from django.shortcuts import render
from.models import places
from.models import highlights
# Create your views here.
def demo(request):
    obj=places.objects.all()
    obj1=highlights.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj1})
